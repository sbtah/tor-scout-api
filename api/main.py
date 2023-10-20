from fastapi import FastAPI
from core.models import Base
from core.database import engine


Base.metadata.create_all(bind=engine)
app = FastAPI(title='Tor Scout API')


@app.get('/')
def read_root():
    return {'message': 'Hi, Welcome to Tor Search API.'}
