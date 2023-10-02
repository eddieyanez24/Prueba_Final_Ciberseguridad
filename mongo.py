from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import requests


import os

load_dotenv()

user = os.getenv("MONGO_USER")
password = os.getenv('MONGO_PASSWORD')

uri = f"mongodb+srv://{user}:{password}@pruebafinal1.jyv6zya.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

url = (
        "https://svc-0-usf.hotyon.com/search?q=&apiKey=e417fce7-fd41-4b57-92a7-10807644a332&getProductDescription=0&locale=es&collection=165868896341&skip=0&take=28&sort=-date")
for item in range(20):
    r = requests.get(url).json()

    articulo = r['data']['items'][item]['tags'][1]
    gener = r['data']['items'][item]['tags'][2]
    color = r['data']['items'][item]['tags'][0]
    tall = r['data']['items'][item]['tags'][3]
    valor = r['data']['items'][item]['variants'][0]['price']
    print(f"{articulo} - {gener} - {color} - {tall} - ${valor}")
    document = {
        "articulo": articulo,
        "genero": gener,
        "color": color,
        'talla': tall,
        "precio": valor
    }
    client.get_database('PruebaFinal').get_collection('Ropa_Segunda_Mano').insert_one(document=document)