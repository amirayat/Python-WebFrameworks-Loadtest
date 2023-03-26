import multiprocessing
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.future import select
from database.dotenv import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT
from database.sqlalchemy_api import Country, to_dict



POSTGRESQL_DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

async def setup_database():
    """
    make database session for fastapi
    """
    engine = create_async_engine(
            POSTGRESQL_DATABASE_URL,
            future=True,
            pool_size=1000//multiprocessing.cpu_count(),
            connect_args={
                "ssl": False  # NEEDED FOR NGINX-UNIT OTHERWISE IT FAILS
            },
        )
    return sessionmaker(engine, class_=AsyncSession)


async def get_countries(session) -> list:
    """
    get all world countries using sqlalchemy async session
    """
    query = select(Country)
    result = await session.execute(query)
    countries : list[Country] = result.scalars().all()
    countries = [to_dict(country) for country in countries]
    return countries


### async engine for sanic
bind = create_async_engine(POSTGRESQL_DATABASE_URL)
_sessionmaker = sessionmaker(bind, class_=AsyncSession, expire_on_commit=False)



