from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'key' : '1222345'}
