import ast
import asyncpg
from database.dotenv import DB_NAME ,DB_TABLE ,DB_USER ,DB_PASSWORD ,DB_HOST ,DB_PORT


async def create_pool(loop=None):
    return await asyncpg.create_pool(
                    min_size=1,
                    max_size=10,
                    command_timeout=60,
                    host=DB_HOST,
                    port=DB_PORT,
                    user=DB_USER,
                    password=DB_PASSWORD,
                    database=DB_NAME,
                    loop=loop
                )

async def get_countries(pool):
    """
    get all world countries using asyncpg api
    """
    async with pool.acquire() as connection:
        values = await connection.fetch(f"""SELECT * FROM {DB_TABLE};""")
        countries = list()
        for record in values:
            record = dict(record)
            for k,v in record.items():
                if k in ["timezones","translations"]:
                    record[k] = ast.literal_eval(v)
            countries.append(record)
        return countries
