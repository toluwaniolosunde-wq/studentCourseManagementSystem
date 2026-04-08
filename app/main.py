# from fastapi import FastAPI
# from app.routes import user_routes
import uvicorn
from fastapi import FastAPI

app = FastAPI()

# app.include_router(user_routes.router)

@app.get("/")
def red_root():
    return {"Hello Students"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

