import psycopg2
import psycopg2.extras
from database.dotenv import DB_NAME, DB_TABLE, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT


conn = psycopg2.connect(f"dbname='{DB_NAME}' user='{DB_USER}' host='{DB_HOST}' password='{DB_PASSWORD}'")

def get_countries():
    """
    get all world countries using psycopg cursor 
    """
    cur = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    cur.execute(f"""SELECT * FROM {DB_TABLE}""")
    countries = cur.fetchall()
    return countries


def connect_get_countries():
    """
    get all world countries using psycopg cursor 
    make new connection on call
    """
    conn = psycopg2.connect(f"dbname='{DB_NAME}' user='{DB_USER}' host='{DB_HOST}' password='{DB_PASSWORD}'")
    cur = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    cur.execute(f"""SELECT * FROM {DB_TABLE}""")
    countries = cur.fetchall()
    return countries




