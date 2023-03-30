import time

import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/109.0.0.0 Safari/537.36'}
query = "메이플스토리"
url = "https://search.danawa.com/dsearch.php?query=" + query
html = requests.get(url, headers=headers).text
soup = BeautifulSoup(html, "html.parser")
product_list = soup.select(".prod_item")
for product in product_list:
    name = product.select_one(".prod_name").text
    try:
        print(name)
    except:
        print("익셉션")
