import json
from japronto import Application
from database.sqlalchemy_api import get_countries, SessionLocal


def get_db():
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()
        del db


def list_countries(request):
    countries = get_countries(get_db())
    return request.Response(text=json.dumps(countries), mime_type='application/json')


app = Application()

r = app.router
r.add_route('/countries/', list_countries)

if __name__ == "__main__":
    app.run('0.0.0.0',8000,worker_num=10)
