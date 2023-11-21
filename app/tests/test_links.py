from httpx import AsyncClient

from app.main import app


async def test_add_new_links(client: AsyncClient):
    response = await client.post(
        app.url_path_for("visited_links"),
        json={
            "links": [
                "https://ya.ru/",
                "https://ya.ru/search/?text=мемы+с+котиками",
                "https://sber.ru",
                "https://stackoverflow.com/questions/65724760/how-it-is",
            ]
        },
    )
    assert response.status_code == 200
    result = response.json()
    assert result["status"] == "ok"


async def test_get_uniq_links_by_time(client: AsyncClient):
    params = {"from_time": 1400000, "to_time": 17000000}
    response = await client.get(app.url_path_for("visited_links"), params=params)
    assert response.status_code == 200
    result = response.json()
    assert result["status"] == "ok"
