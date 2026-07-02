from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from enum import Enum


class TodoStatus(str, Enum):
    PENDING = "pending"
    IN_PROGRESS = "in-progress"
    COMPLETED = "completed"


class TodoCreate(BaseModel):
    id: int
    title: str
    description: str
    status: TodoStatus


todos = []
current_id = 1

app = FastAPI(title="To-do App")


@app.get("/todos")
def get_todos():
    return todos


@app.get("/todos/{current_id}")
def get_single_todo(current_id: int):
    for todo in todos:
        if todo.id == current_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")


@app.post("/todos")
def create_todo(todo: TodoCreate):
    global current_id

    todo.id = current_id
    todos.append(todo)
    current_id += 1
    return todo


@app.put("/todos/{current_id}")
def update_single_todo(current_id: int, updated_data: TodoCreate):
    for todo in todos:
        if todo.id == current_id:
            todo.title = updated_data.title
            todo.description = updated_data.description
            todo.status = updated_data.status
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")


@app.delete("/todos/{current_id}")
def delete_todo(current_id: int):
    for todo in todos:
        if todo.id == current_id:
            todos.remove(todo)
            return {"message": "Successfully deleted!!!"}
    raise HTTPException(status_code=404, detail="Todo not found")
