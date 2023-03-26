from contextvars import ContextVar
from sanic import Sanic, json
from database.sqlalchemy_async_api import _sessionmaker, get_countries


app = Sanic(name=__name__) 


_base_model_session_ctx = ContextVar("session")


@app.middleware("request")
async def inject_session(request):
    request.ctx.session = _sessionmaker()
    request.ctx.session_ctx_token = _base_model_session_ctx.set(request.ctx.session)


@app.middleware("response")
async def close_session(request, response):
    if hasattr(request.ctx, "session_ctx_token"):
        _base_model_session_ctx.reset(request.ctx.session_ctx_token)
        await request.ctx.session.close()


@app.get("/countries/")
async def list_countries(request):
    session = request.ctx.session
    async with session.begin():
        countries = await get_countries(session)
        return json(countries)


if __name__ == "__main__":
    app.run('0.0.0.0', 8000, access_log=False, workers=10)
