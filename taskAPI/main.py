from fastapi import FastAPI,APIRouter,HTTPException
from configuration import item_collection,user_collection
from pymongo.server_api import ServerApi


app=FastAPI()
router=APIRouter()
   

@router.get("/items/")
def item_list():
  data=list(item_collection.find())
  for item in data:
        item["_id"] = str(item["_id"])
  return data


@router.post("/create_items/")
def item_create(name:str,price:int):
   try:
       item_data={"name":name,
                  "price":price}
       resp=item_collection.insert_one(item_data)
       return{"status_code": 200,"id":str(resp.inserted_id)}
   except Exception as e:
       return HTTPException(status_code=500, detail=f"Some error occured {e}")
   

@router.get("/users/")
def user_list():
  data=list(user_collection.find())
  for item in data:
        item["_id"] = str(item["_id"])
  return data


@router.post("/create_users/")
def user_create(name:str,balance:int):
   try:
       user_data={"name":name,
                  "balance":balance}
       resp=user_collection.insert_one(user_data)
       return {"status_code": 200,"id":str(resp.inserted_id)}
   except Exception as e:
       return HTTPException(status_code=500, detail=f"Some error occured {e}")
   
    
app.include_router(router)