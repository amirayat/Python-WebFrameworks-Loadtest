import logging
from flask import Flask, jsonify
from database.psycopg_api import get_countries


app = Flask(__name__)
logging.getLogger('werkzeug').disabled = True


@app.route("/countries/")
def home():
    countries = get_countries()
    return jsonify(countries)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)