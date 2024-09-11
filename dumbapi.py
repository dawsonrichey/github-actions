from fastapi import FastAPI
import string
import random

app = FastAPI()


@app.get("/")
async def index():
    mystring = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    return {"data": mystring}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}