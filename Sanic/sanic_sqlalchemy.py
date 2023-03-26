from sanic import Sanic, json
from database.sqlalchemy_api import SessionLocal, get_countries


def get_db():
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()
        del db


app = Sanic(name=__name__) 


@app.get("/countries/")
def list_countries(request):
    countries = get_countries(get_db())
    return json(countries)


if __name__ == "__main__":
    app.run('0.0.0.0', 8000, access_log=False, workers=10)
