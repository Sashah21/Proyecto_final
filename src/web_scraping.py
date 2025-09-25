from bs4 import BeautifulSoup

def get_scrapping(producto:str):
    url = 'https://www.carrefour.es/?query='
    url += '%20'.join(producto)
    print(url)

get_scrapping('salsa de soja')