from fastapi import FastAPI,HTTPException
import json
from configrations import collection
from bson import ObjectId
from pydantic import BaseModel
from datetime import datetime
app=FastAPI()


@app.get("/")
def index():
    data=collection.find()
    return all(data)

@app.post("/create_task")
def create_task():
    try:
        with open("task.json", "r") as file:
            task_data = json.load(file)

        result = collection.insert_one(task_data)
        if result.inserted_id:
            return {"message": "Task created successfully from file", "task_id": str(result.inserted_id)}
        else:
            return HTTPException(status_code=500, detail="Task creation failed")
        
    except FileNotFoundError:
        return HTTPException(status_code=404, detail="JSON file not found")
    
    except json.JSONDecodeError:
        return HTTPException(status_code=400, detail="Invalid JSON format")


@app.put("/{task_id}") 
def update_task(task_id:str, updated_task:dict):
    try:
       id=ObjectId(task_id)
       exesting_doc = collection.find_one({"_id":id})
       if not exesting_doc:
           return HTTPException(status_code=404, detail=f"Task does not exits")
    
       updated_task["updated_at"]= datetime.timestamp(datetime.now())
       print(updated_task)
       resp=collection.update_one({"_id":id}, {"$set":updated_task})
       
       return{"status_code":200,"message":"Task Updated Sucessfully"}
    except Exception as e:
       return HTTPException(status_code=500, detail=f"Some error occured {e}")
    

@app.delete("/permanent_delete/{task_id}") 
def update_task(task_id:str):
    try:
       id=ObjectId(task_id)
       exesting_doc = collection.find_one({"_id":id})
       if not exesting_doc:
           return HTTPException(status_code=404, detail=f"Task does not exits")

       resp=collection.delete_one({"_id":id})
       return{"status_code":200,"message":"Task deleted Sucessfully"}
    
    except Exception as e:
       return HTTPException(status_code=500, detail=f"Some error occured {e}")