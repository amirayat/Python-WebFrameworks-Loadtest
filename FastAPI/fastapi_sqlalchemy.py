import uvicorn
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database.sqlalchemy_api import SessionLocal, get_countries


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        del db


app = FastAPI()


@app.get("/countries/")
def list_countries(db: Session = Depends(get_db)):
    countries = get_countries(db)
    return countries


if __name__ == "__main__":
    uvicorn.run("fastapi_sqlalchemy:app", host="0.0.0.0", port=8000, workers=10, log_level='critical')
