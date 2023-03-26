import motor.motor_asyncio
from database.dotenv import DB_NAME, DB_COLLECTION, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT


client = motor.motor_asyncio.AsyncIOMotorClient(f'mongodb://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/')
db = client[DB_NAME]
col = db[DB_COLLECTION]


async def get_countries():
    """
    get all world countries using pymongo cursor
    """
    countries = await col.find({},{'_id':0}).to_list(250)
    # countries = list(countries)
    return countries