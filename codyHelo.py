from fastapi import FastAPI
import string
import random
import time

app = FastAPI()

urls = [
    "https://example.com",
    "https://google.com",
    "https://github.com",
    "https://stackoverflow.com",
    "https://python.org"
]

@app.get("/")
async def index():
    start_time = time.time()
    mystring = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    execution_time = time.time() - start_time
    return {"data": mystring, "execution_time": execution_time}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    start_time = time.time()
    if 0 <= item_id < len(urls):
        result = {"item_id": item_id, "url": urls[item_id]}
    else:
        result = {"error": "Invalid item_id"}
    execution_time = time.time() - start_time
    result["execution_time"] = execution_time
    return result
