import requests
from bs4 import BeautifulSoup

count = 10

#스킨케어
category_no1 = "10000010001"
#클렌징
category_no2 = "10000010010"
#남성용
category_no3 = "10000010007"
response = requests.get("https://www.oliveyoung.co.kr/store/main/getBestList.do?dispCatNo=900000100100001&fltDispCatNo=" + category_no3)
if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    product_list = soup.select(".prd_info")
    for i in range(count):
        print(product_list[i].select_one(".tx_name").text)
        print(product_list[i].find("img")['src'])
        print(product_list[i].select_one(".tx_cur").text)
        link = product_list[i].find("a")["href"]
        link_response = requests.get(link).text
        print(link)
        link_soup = BeautifulSoup(link_response, "html.parser")
        rank = link_soup.select_one("#repReview")
        print(rank.find("b").text.strip(), rank.find("em").text.strip())


else:
    print("오류 발생")