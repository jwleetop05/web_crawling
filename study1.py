import requests
from bs4 import  BeautifulSoup
# https://jsonplaceholder.typicode.com/users/1


resource = requests.get("http://www.sdh.hs.kr/")
html = resource.text
soup = BeautifulSoup(html, "html.parser")
# print(soup.find(attrs={'class':'img-box'}))
# print(soup.find_all("a", "img-box"))
images = soup.find_all("a", "img-box")

for i in images:
    print(i)
    if i.find(attrs={"alt": "ko-text"}):
        print(i['href'])
