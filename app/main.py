import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def red_root():
    return {"Hello Students"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return

