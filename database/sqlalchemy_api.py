from sqlalchemy import create_engine, BigInteger, Column, Identity, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.dialects.postgresql import JSONB
from database.dotenv import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT



POSTGRESQL_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(POSTGRESQL_DATABASE_URL, pool_size=100, max_overflow=0)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Country(Base):
    """
    world countries model
    """
    __tablename__ = 'countries'

    id = Column(BigInteger, Identity(start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), primary_key=True)
    name = Column(String(36), nullable=False)
    iso3 = Column(String(3), nullable=False)
    iso2 = Column(String(2), nullable=False)
    numeric_code = Column(String(3), nullable=False)
    phone_code = Column(String(16), nullable=False)
    currency = Column(String(3), nullable=False)
    currency_name = Column(String(39), nullable=False)
    currency_symbol = Column(String(6), nullable=False)
    tld = Column(String(3), nullable=False)
    timezones = Column(JSONB, nullable=False)
    translations = Column(JSONB, nullable=False)
    latitude = Column(String(12), nullable=False)
    longitude = Column(String(13), nullable=False)
    emoji = Column(String(2), nullable=False)
    emojiU = Column(String(15), nullable=False)
    capital = Column(String(20))
    native = Column(String(50))
    region = Column(String(8))
    subregion = Column(String(25))


def to_dict(country: Country) -> dict:
    """
    convert model object to dict
    """
    country_dict = {
        "id": country.id,  
        "name": country.name,  
        "iso3": country.iso3,  
        "iso2": country.iso2,  
        "numeric_code": country.numeric_code,  
        "phone_code": country.phone_code,  
        "currency": country.currency,  
        "currency_name": country.currency_name,  
        "currency_symbol": country.currency_symbol,  
        "tld": country.tld,  
        "timezones": country.timezones,  
        "translations": country.translations,  
        "latitude": country.latitude,  
        "longitude": country.longitude, 
        "emoji": country.emoji, 
        "emojiU": country.emojiU, 
        "capital": country.capital,  
        "native": country.native,  
        "region": country.region,  
        "subregion": country.subregion
    }
    return country_dict


def get_countries(db: Session):
    """
    get all world countries using sqlalchemy session
    """
    countries = [to_dict(country) for country in db.query(Country).all()]
    return countries
