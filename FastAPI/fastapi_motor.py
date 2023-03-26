import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from database.motor_api import get_countries


app = FastAPI() 


@app.get("/countries/")
async def list_countries():
    countries = await get_countries()
    return JSONResponse(countries)


if __name__ == "__main__":
    uvicorn.run("fastapi_motor:app", host="0.0.0.0", port=8000, workers=10, log_level='critical')
