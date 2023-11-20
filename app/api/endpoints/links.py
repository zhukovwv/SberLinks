from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Dict
import time
from sqlalchemy import select
from starlette.responses import JSONResponse

from app.api import deps
from app.models import Link
from typing import Optional


router = APIRouter()


@router.post("/visited_links")
async def visited_links(
    links: Dict,
    session: AsyncSession = Depends(deps.get_session),
):
    current_time_seconds = int(time.time())
    try:
        for link in links.get("links", []):
            new_link = Link(url=link, time_visited=current_time_seconds)
            session.add(new_link)

        await session.commit()

        return JSONResponse(content={"status": "ok"})
    except Exception as e:
        await session.rollback()
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
    finally:
        await session.close()


@router.get("/visited_links")
async def visited_links(
        from_time: Optional[int] = Query(None, title="From Time", description="Unix timestamp"),
        to_time: Optional[int] = Query(None, title="To Time", description="Unix timestamp"),
        session: AsyncSession = Depends(deps.get_session),
):
    try:
        stmt = select(Link.url).distinct()
        if from_time is not None:
            stmt = stmt.where(Link.time_visited >= from_time)
        if to_time is not None:
            stmt = stmt.where(Link.time_visited <= to_time)

        domains = [result[0] for result in await session.execute(stmt)]

        return JSONResponse(content={"domains": domains, "status": "ok"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
    finally:
        await session.close()
