import json
from japronto import Application
from database.pymongo_api import get_countries


def list_countries(request):
    countries = json.dumps(get_countries())
    return request.Response(text=countries, mime_type='application/json')


app = Application()

r = app.router
r.add_route('/countries/', list_countries)

if __name__ == "__main__":
    app.run('0.0.0.0',8000,worker_num=10)
