from bs4 import BeautifulSoup
import requests

for i in range(1,18):
    html = requests.get("https://stickker.net/magaza/page/%d" % i ).content

    bs = BeautifulSoup(html,"html.parser")
    product_ul = bs.find("ul",{"class":"products"})

    products = product_ul.find_all("li")
    for product in products:
        print(product.find("img")["src"])
        print(product.find("h2").text)
        print(product.find("span",{"class":"amount"}).text)