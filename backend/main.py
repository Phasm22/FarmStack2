from http.client import HTTPException
from model import Todo
from database import (
    fetch_all_todos, fetch_one_todo, remove_todo, create_todo, update_todo
)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


# python -m uvicorn main:app --reload
# Object
app = FastAPI()


origins = ['http://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get('/')
def read_root():
    return {"Ping": "pong"}


@app.get("/api/todo")
async def get_todo():
    response = await fetch_all_todos()
    return response


@app.get("/api/todo/{name}", response_model=Todo)
async def get_todo_by_id(name):
    response = fetch_one_todo(name)
    if response:
        return response
    raise HTTPException(
        404, f"There is no person with this name: {name} ")


@app.post("/api/todo/", response_model=Todo)
async def post_todo(todo: Todo):
    response = await create_todo(todo.dict())
    if response:
        return response
    raise HTTPException(404, "Something went wrong / Bad Request")


@app.put("/api/todo/{name}", response_model=Todo)
async def put_todo(name: str, dept: str):
    response = await update_todo(name, dept)
    if response:
        return response
    raise HTTPException(404, f"There is no person with this name: {name} ")


@app.delete("/api/todo/{name}")
async def delete_todo(name):
    response = await remove_todo(name)
    if response:
        return "Succesfully deleted item"

    raise HTTPException(404, f"There is no person with this name: {name} ")
