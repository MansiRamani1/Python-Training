from fastapi import FastAPI,APIRouter,HTTPException
from configuration import collection
from pymongo.server_api import ServerApi


app=FastAPI()
router=APIRouter()
   

@router.get("/")
def list_item():
  data=collection.find()
  return data


@router.post("/")
def create_item(new_task:dict):
   try:
       resp=collection.insert_one(new_task)
       return{"status_code": 200, "id":str(resp.inserted_id)}
   except Exception as e:
       return HTTPException(status_code=500, detail=f"Some error occured {e}")
    
app.include_router(router)