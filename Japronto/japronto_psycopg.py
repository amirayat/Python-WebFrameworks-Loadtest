import json
from japronto import Application
from database.psycopg_api import connect_get_countries


def list_countries(request):
    countries = json.dumps(connect_get_countries())
    return request.Response(text=countries, mime_type='application/json')


app = Application()

r = app.router
r.add_route('/countries/', list_countries)

if __name__ == "__main__":
    app.run('0.0.0.0',8000,worker_num=10)
