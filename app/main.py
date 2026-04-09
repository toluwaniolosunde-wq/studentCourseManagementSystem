from fastapi import FastAPI
from app.routes import enrollment_routes
from app.routes import user_routes
from app.routes import course_routes

app = FastAPI()

app.include_router(enrollment_routes.router)
app.include_router(user_routes.router)
app.include_router(course_routes.router)

app = FastAPI()

app.include_router(enrollment_routes.router)


@app.get("/")
def red_root():
    return {"Hello Students"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}






