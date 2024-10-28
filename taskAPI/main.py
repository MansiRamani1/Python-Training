from fastapi import FastAPI,APIRouter,HTTPException
from configuration import db,user_collection,user_item_collection,purchase_collection,sell_collection
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
from datetime import datetime

app=FastAPI()
router=APIRouter()
   

@router.get("/items/")
def item_list():
  data=list(db["item_master"].find())#data=list(item_collection.find())
  for item in data:
        item["_id"]=str(item["_id"])#return data json format
  return data



# @router.post("/create_items/")
# def item_create(name:str,price:int):
#    try:
#        item_data={"name":name,
#                   "price":price}
#        resp=db["item_master"].insert_one(item_data)
#        return{"status_code": 200,"id":str(resp.inserted_id)}
#    except Exception as e:
#        return HTTPException(status_code=500, detail=f"Some error occured {e}")

@router.post("/create_items")
def item_create(item_data:dict):
   try:
       resp=db["item_master"].insert_one(item_data)
       return{"status_code": 200,"id":str(resp.inserted_id)}
   except Exception as e:
       return HTTPException(status_code=500, detail=f"Some error occured {e}")  

@router.get("/users/")
def user_list():
  data=list(user_collection.find())
  for item in data:
        item["_id"]=str(item["_id"])
  return data


@router.post("/create_users")
def user_create(user_data:dict):
   try:
      #  user_data={"name":name,
      #             "balance":balance}
       resp=user_collection.insert_one(user_data)
       return {"status_code": 200,"id":str(resp.inserted_id)}
   except Exception as e:
       return HTTPException(status_code=500, detail=f"Some error occured {e}")

@router.post("/purchase_item")
def purchase_item(item_id:str,user_id:str):
    try:
        item_find=db["item_master"].find_one({"_id":ObjectId(item_id)})
        print(item_find)
        user_find=user_collection.find_one({"_id":ObjectId(user_id)})
        # print(item_find)
        if not item_find:
            return HTTPException(status_code=404, detail=f"Task does not exits")
        if not user_find:
            return HTTPException(status_code=404, detail=f"Task does not exits")

        if user_find["balance"]==0:
            return HTTPException("your balance is zero!!,can't purchase")
        
        if user_find["balance"]<item_find["price"]:
            return HTTPException("can't purchase")

        purchase_item_price=item_find["price"]
        current_balance=user_find["balance"]-purchase_item_price
        print(current_balance)
        user_collection.update_one({"_id":user_id},{"$set":{"balance":current_balance}})

        purchaseitem={
                       "user_id":user_find["_id"],
                       "item_id":item_find["_id"],
                       "created_at":int(datetime.timestamp(datetime.now()))
        }
        
        user_item_collection.insert_one({"user_id":user_id,"item_id":item_id})
        
        purchase_collection.insert_one(purchaseitem)

        payload={
                  "user":user_find["Name"],
                  "item":item_find["item"],
                  "created_at":purchaseitem["created_at"]}
        
        return{"status_code":200,"message":"Purchase Sucessfully","payload":payload}    
    
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Some error occured {e}")
    
@router.get("/user_purchased_item_list")
def user_item_list(user_id:str):
  try:
      user=list(user_item_collection.find({"user_id":user_id}))
    
      if not user:
            return HTTPException(status_code=404, detail=f"Task does not exits")

      payload=[]
      for user_item in user:
                item=db["item_master"].find_one({"_id":ObjectId(user_item["item_id"])})
                if item:
                    item["_id"]=str(item["_id"]) #objectid to string
                    payload.append(item)
      return payload
  except Exception as e:
        return HTTPException(status_code=500, detail=f"Some error occured {e}")
    
           

@router.post("/sell_items")
def user_sell_item(user_id:str,item_id:str):
    try:
        user=user_collection.find_one({"_id":ObjectId(user_id)})
        item=db["item_master"].find_one({"_id":ObjectId(item_id)})
        
        if not user:
            return HTTPException(status_code=404, detail=f"Task does not exits")
        
        if not item:
            return HTTPException(status_code=404, detail=f"Task does not exits")
        
        purchased_items=user_item_collection.find_one({"user_id":user_id,"item_id":item_id})
        
        if not purchased_items:
            return HTTPException(status_code=404, detail="User has not purchased any item")
        
        update_balance=user["balance"]+item["price"]
        user_collection.update_one({"_id":user_id},{"$set":{"balance":update_balance}})

        user_item_collection.delete_one({"user_id": user_id, "item_id": item_id})
        sellitem={
                       "user_id":user["_id"],
                       "item_id":item["_id"],
                       "created_at":int(datetime.timestamp(datetime.now()))
        }   
        existing_doc=sell_collection.insert_one(sellitem)

        payload={
                  "user":user["Name"],
                  "item":item["item"],
                  "created_at":sellitem["created_at"]}
        
        return{"status_code":200,"message": "sell item successfully" ,"payload":payload}
	   
    except Exception as e:
            return HTTPException(status_code=500, detail=f"Some error occured{e}")
    

app.include_router(router)