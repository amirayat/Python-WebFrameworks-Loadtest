import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from database.asyncpg_api import create_pool, get_countries


app = FastAPI()

@app.on_event("startup")
async def startup():
    global pool
    pool = await create_pool()


@app.get("/countries/")
async def list_countries():
    countries = await get_countries(pool)
    return JSONResponse(countries)


if __name__ == "__main__":
    uvicorn.run("fastapi_asyncpg:app", host="0.0.0.0", port=8000, workers=10, log_level='critical')
