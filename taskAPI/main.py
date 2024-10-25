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
        item["_id"] = str(item["_id"])#return data json format
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
        item["_id"] = str(item["_id"])
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
   

# @router.get("/item_user_map/")
# def user_list_map():
#   data=list(user_item_collection.find())
#   for item in data:
#         item["_id"] = str(item["_id"])
#   return data


# @router.post("/items_users")
# def user_item(user_id:str,item_id):
#    try:
#        resp=user_item_collection.insert_one(user_id,item_id)
#        return {"status_code": 200,"id":str(resp.inserted_id)}
#    except Exception as e:
#        return HTTPException(status_code=500, detail=f"Some error occured {e}")


@router.post("/purchase_item")
def purchase_item(item_id:str,user_id:str):
    try:
        item_find=db["item_master"].find_one({"_id":ObjectId(item_id)})
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
        
        user_item_collection.insert_one({"user_id":user_id,"item_id": item_id})
        
        existing_doc=purchase_collection.insert_one(purchaseitem)
        return{"status_code":200,"message":"Purchase Sucessfully"}    
    
    except Exception as e:
            return HTTPException(status_code=500, detail=f"Some error occured {e}")


@router.post("/show_user_item")
def purchase_item_list(user_id:str,item_id:str):
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
        purchaseitem={
                       "user_id":user["_id"],
                       "item_id":item["_id"],
                       "created_at":int(datetime.timestamp(datetime.now()))
        }   
        print(purchaseitem)    
        existing_doc=sell_collection.insert_one(purchaseitem)
        return{"status_code":200,"message": "get successfully",
	    #  "payload":[
		#    {
		# 	"item_id":"6718b7667de3d1cbf7e8c459",
		# 	"item_name":"shoes"
		#    },
		#    {
		# 	"item_id":"6718b7417de3d1cbf7e8c458",
		# 	"item_name":"chia"
		#    }
	    #   ]
         }  
    except Exception as e:
            return HTTPException(status_code=500, detail=f"Some error occured{e}")
           
app.include_router(router)