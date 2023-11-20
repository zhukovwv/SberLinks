FROM python:3.12

ENV PYTHONUNBUFFERED 1
WORKDIR /build

RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt

RUN pip install uvicorn[standard]

COPY app app
COPY alembic alembic
COPY alembic.ini .
COPY pyproject.toml .
COPY init.sh .

RUN addgroup --gid 1001 --system uvicorn && \
    adduser --gid 1001 --shell /bin/false --disabled-password --uid 1001 uvicorn

RUN chown -R uvicorn:uvicorn /build
CMD bash init.sh && \
    runuser -u uvicorn -- /venv/bin/uvicorn app.main:app --app-dir /build --host 0.0.0.0 --port 8000 --workers 2 --loop uvloop
EXPOSE 8000