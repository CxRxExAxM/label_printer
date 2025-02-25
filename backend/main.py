from fastapi import FastAPI
from app.api import app as api_app

app = FastAPI()

app.mount('/api', api_app)

@app.get('/')
def read_root():
    return {'message': 'Resort Label Printer'}
