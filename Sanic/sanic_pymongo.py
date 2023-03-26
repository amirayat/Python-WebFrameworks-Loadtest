from sanic import Sanic, json
from database.pymongo_api import get_countries


app = Sanic(name=__name__) 


@app.get("/countries/")
def list_countries(request):
    countries = get_countries()
    return json(countries)


if __name__ == "__main__":
    app.run('0.0.0.0', 8000, access_log=False, workers=10)
