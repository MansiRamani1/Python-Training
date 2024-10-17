
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import ssl
import certifi
from pymongo import MongoClient
from urllib.parse import quote_plus


username = quote_plus("mansi")  
password = quote_plus("Mansi@123") 
uri = f"mongodb+srv://{username}:{password}@cluster0.jnepj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi('1'))
            
db=client.task_imp
item_collection=db["item_master"]
user_collection=db["user_master"]