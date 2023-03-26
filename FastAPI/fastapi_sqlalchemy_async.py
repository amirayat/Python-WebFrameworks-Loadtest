import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI
from database.sqlalchemy_async_api import get_countries, setup_database


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.db_session = await setup_database()
    yield
    await app.state.db_session.close()


app = FastAPI(lifespan=lifespan)


@app.get("/countries/")
async def list_countries():
    async with app.state.db_session() as session:
        countries = await get_countries(session)
    return countries


if __name__ == "__main__":
    uvicorn.run("fastapi_sqlalchemy_async:app", host="0.0.0.0", port=8000, workers=10, log_level='critical')
