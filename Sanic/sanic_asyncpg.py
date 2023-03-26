from sanic import Sanic, json
from database.asyncpg_api import create_pool, get_countries


app = Sanic(name=__name__) 


@app.listener("before_server_start")
async def startup(app, loop):
    app.config['pool'] = await create_pool()


@app.get("/countries/")
async def list_countries(request):
    pool = request.app.config['pool']
    countries = await get_countries(pool)
    return json(countries)


if __name__ == "__main__":
    app.run('0.0.0.0', 8000, access_log=False, workers=10)
