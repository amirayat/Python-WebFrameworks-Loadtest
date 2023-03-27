import os
import json
from pathlib import Path
from pymongo import MongoClient
from dotenv import load_dotenv


load_dotenv()

DB_NAME = os.getenv('DB_NAME')
DB_COLLECTION = os.getenv('DB_COLLECTION')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = int(os.getenv('DB_PORT'))


DIR = str(Path(__file__).resolve().parent)
COUNTRIES_PATH = DIR + '/countries.json'


client = MongoClient(f'mongodb://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/')
db = client[DB_NAME]
col = db[DB_COLLECTION]

client.drop_database(DB_NAME)

def insert_countries():
    with open(COUNTRIES_PATH) as fp:
        data = json.load(fp)
        col.insert_many(data)

insert_countries()

