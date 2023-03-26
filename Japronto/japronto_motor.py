import json
from japronto import Application
from database.motor_api import get_countries


async def list_countries(request):
    countries = await get_countries()
    return request.Response(text=json.dumps(countries), mime_type='application/json')


app = Application()

r = app.router
r.add_route('/countries/', list_countries)

if __name__ == "__main__":
    app.run('0.0.0.0',8000,worker_num=10)
