

from typing import Union

from fastapi import FastAPI,APIRouter,HTTPException
from configrations import collection
from database.schemas import all_tasks
from database.models import Todo
from bson.objectid import ObjectId
from datetime import datetime

app = FastAPI()
router=APIRouter()

# @app.get("/")
# def read_root():
#     return {"Hello": "Mansi"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}
@router.get("/")
def get_all_todos():
  data=collection.find()
  return all_tasks(data)

@router.post("/")
def create_task(new_task : Todo):
   try:
       resp = collection.insert_one(dict(new_task))
       return{"status_code": 200, "id":str(resp.inserted_id)}
   except Exception as e:
       return HTTPException(status_code=500, detail=f"Some error occured {e}")

@router.put("/{task_title}") 
def update_task(task_title:str, updated_task:dict):
    try:
       print(updated_task)
       exesting_doc = collection.find_one({"title":task_title, "is_deleted": False})
       if not exesting_doc:
           return HTTPException(status_code=404, detail=f"Task does not exits")
       
    #    update_task={}
    #    if updated_task.title: #check title , if not empty then move to next condition,
    #        update_task["title"]=updated_task.title

       updated_task["updated_at"]= datetime.timestamp(datetime.now())
       print(updated_task)
       resp=collection.update_one({"title":task_title}, {"$set":updated_task})
       
       return{"status_code":200,"message":"Task Updated Sucessfully"}
    except Exception as e:
       return HTTPException(status_code=500, detail=f"Some error occured {e}")
    
@router.put("/tasks/{task_id}") 
def update_task(task_id:str, updated_task: Todo):
    try:
       id=ObjectId(task_id)
       exesting_doc = collection.find_one({"_id":id, "is_deleted": False})
       if not exesting_doc:
           return HTTPException(status_code=404, detail=f"Task does not exits")
       updated_task.updated_at = datetime.timestamp(datetime.now())
       
       resp=collection.update_one({"_id":id}, {"$set":{"title": updated_task.title,"description": updated_task.description}})
       return{"status_code":200,"message":"Task Updated Sucessfully"}
    except Exception as e:
       return HTTPException(status_code=500, detail=f"Some error occured {e}")
    
@router.delete("/{task_id}")
def delete_task(task_id:str):
   try:
       id=ObjectId(task_id)
       exesting_doc = collection.find_one({"_id": id, "is_deleted": False})
       if not exesting_doc:
           return HTTPException(status_code=404, detail=f"Task does not exits")
       resp=collection.update_one({"_id":id}, {"$set":{"is_deleted":True}})
      
       return{"status_code":200,"message":"Task Deletd Sucessfully"}
   
   except Exception as e:
       return HTTPException(status_code=500, detail=f"Some error occured {e}")

@router.delete("/permanent_delete/{task_id}")
def delete_task(task_id:str):
   try:
       id=ObjectId(task_id)
       exesting_doc = collection.find_one({"_id": id})
       if not exesting_doc:
           return HTTPException(status_code=404, detail=f"Task does not exits")
       collection.delete_one({"_id":id})
       return{"status_code":200,"message":"Task Deletd Sucessfully"}
   except Exception as e:
       return HTTPException(status_code=500, detail=f"Some error occured {e}")



app.include_router(router)

