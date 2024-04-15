import requests
#import json

from bs4 import BeautifulSoup



def par(url):
    books = {}

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    data = soup.find_all("div", class_="catalog-grid__item")
    count_page = len(soup.find_all('li', class_="page-navigation__item"))

    for i in range(1, count_page + 1):
        books[i] = {}
        for j in range(1, len(data)+ 1):
            books[i][j] = {}

    for count in range(1, count_page+1):
        url_stra = url + "?cpage=page-"
        url_stra = f"{url_stra}{count}"
        response_stra = requests.get(url_stra)
        soup_stra = BeautifulSoup(response_stra.text, "lxml")
        data_silk = soup_stra.find_all("div", class_="catalog-grid__item")

        num = 1
        for i in data_silk:
            name = i.find("div", class_="product-card-title").text
            price = i.find("div", class_="product-card-price").text
            

            books[count][num] = {
                "name": name,
                "price": price
            } 

            num += 1

    return books


# for i in aboba.keys():
#     for j in aboba[i]:
#         print(f"""name: {aboba[i][j]["name"]}
# price: {aboba[i][j]["price"]}""")


    # knigi = par(url = "https://www.bookcity.kz/khudozhestvennaya-literatura-66108/?cpage=page-1")

    # with open("klasik-liter.json", 'w', encoding="utf-8") as file:
    #     json.dump(knigi, file, ensure_ascii=False, indent=4)

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



    