import logging
from flask import Flask, jsonify
from database.sqlalchemy_api import SessionLocal, get_countries



def get_db():
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()
        del db

app = Flask(__name__)
logging.getLogger('werkzeug').disabled = True


@app.route("/countries/")
def home():
    countries = get_countries(get_db())
    return jsonify(countries)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)