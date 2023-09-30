import requests
from mongo import client


def get_item(item):
    url = (
        "https://svc-0-usf.hotyon.com/search?q=&apiKey=e417fce7-fd41-4b57-92a7-10807644a332&getProductDescription=0"
        "&locale=es&collection=165868896341&skip=0&take=28&sort=-date")

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
    return document


def set_item(document: dict):
    _ = client.get_database('PruebaFinal').get_collection('PruebaFinal').insert_one(document={"marca": "opel", "modelo": "omega"})
    return 'ok'
