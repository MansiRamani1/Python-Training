
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import ssl
import certifi
from pymongo import MongoClient
from urllib.parse import quote_plus


username = quote_plus("mansi")  # No special characters, but it's good practice to always encode
password = quote_plus("Mansi@123") 
uri = f"mongodb+srv://{username}:{password}@cluster0.jnepj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# uri = "mongodb+srv://ramanimansi9:hKLkhTTY2faI83C7@cluster0.bbgwp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# # Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'),tlsCAFile=certifi.where())

# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)
db=client.todo_db
collection=db["todo_data"]