import requests
#import json

from bs4 import BeautifulSoup

url = "https://www.bookcity.kz/khudozhestvennaya-literatura-66108/"

def par_new(url):
    spisok_new = {}
    for i in range(1, 26):
        spisok_new[i] = {}


    num = 1

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    data = soup.find_all("div", class_="catalog-grid__item")

    for i in data:
        name = i.find("div", class_="product-card-title").text
        price = i.find("div", class_="product-card-price").text

        spisok_new[num] = {
            "name": name,
            "price": price
        }

        num += 1
    return spisok_new

spisok = par_new(url=url)
for i in spisok.keys():
    print(f'''{spisok[i]["name"]} 
{spisok[i]["price"]}''')