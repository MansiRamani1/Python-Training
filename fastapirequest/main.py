from fastapi import FastAPI
from typing import List
from pydantic import BaseModel

app=FastAPI()

class Todo(BaseModel):
    title:str
    description:str

@app.get("/first")
def indx():
    return "Hello World!!" 

@app.get("/items/{item_id}")
def index(item_id:int):
    return{"product_id": item_id}

#http://127.0.0.1:8000/items/23            path parameter

@app.get("/items/")
def index(q:int=None,p:int=None,m:List[int]=10):
    return{"product is":q,"p":p,"m":m}

# http://127.0.0.1:8000/items/?q=10        query parameter


@app.get("/items/{file_path:path}")
def index(file_path:str):
    return{"file_path":file_path}

# http://127.0.0.1:8000/items/jhmmm/  filepath