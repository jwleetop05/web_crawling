import requests
from bs4 import BeautifulSoup

response = requests.get("http://www.cgv.co.kr/movies/?lt=1&ft=0")
if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    section = soup.select(".sect-movie-chart")
    movie_section = section[0]
    movies = movie_section.find_all("li")
    for movie in movies:
        rank = movie.select_one(".rank").text.split(".")
        print(rank[1], "위")
        print(movie.find("img")["src"])
        print(movie.select_one(".title").text)
        print(movie.select_one(".percent").text)
        print("https://www.cgv.co.kr" + movie.select_one(".link-reservation")["href"])
else:
    print("오류 발생")
