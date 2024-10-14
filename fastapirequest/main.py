from fastapi import FastAPI
from typing import List
from pydantic import BaseModel

app=FastAPI()

class Todo(BaseModel):
    title:str
    description:str

tasks = {
    "Task1":{"title":"Task1","description":"Python Learning"},
    "Task2":{"title":"Task2","description":"Get Title"},
    "Task3":{"title":"Task3","description":"Get description"},
}

# @app.get("/first")
# def indx():
#     return "Hello World!!" 

# @app.get("/items/{item_id}")
# def index(item_id:int,Todo):
#     return{"product_id": item_id}

# #http://127.0.0.1:8000/items/23            path parameter

# @app.get("/items/")
# def index(q:int=None,p:int=None,m:List[int]=10):
#     return{"product is":q,"p":p,"m":m}

# # http://127.0.0.1:8000/items/?q=10        query parameter


# @app.get("/items/{file_path:path}")
# def index(file_path:str):
#     return{"file_path":file_path}

# # http://127.0.0.1:8000/items/jhmmm/  filepath

@app.get("/items/{title}")
def get_title(title:str):
    if title in tasks:
        #return tasks[title]
        return {"description":tasks[title]["description"]}
    else:
        return {"404":"Task not found"}