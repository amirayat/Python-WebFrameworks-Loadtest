from pymongo import MongoClient
from database.dotenv import DB_NAME, DB_COLLECTION, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT



client = MongoClient(f'mongodb://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/')
db = client[DB_NAME]
col = db[DB_COLLECTION]


def get_countries():
    """
    get all world countries using pymongo cursor
    """
    countries = list(col.find({},{'_id':0}))
    return countries
