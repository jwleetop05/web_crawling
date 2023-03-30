import requests
from bs4 import BeautifulSoup


def new_movies():
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


def search_movie_poster(movie_name):
    # encoded_string = str(movie_name.encode('unicode_escape')).upper().replace('B'', '').replace(''', '').replace('\\U','%u')
    response = requests.get("http://www.cgv.co.kr/search/?query=" + movie_name)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        section = soup.select(".searchingMovieResult_list")
        movie_section = section[0]
        movies = movie_section.find_all("li")
        for movie in movies:
            print(movie.find("img")["src"])
            print(movie.select_one(".searchingMovieName").text)
            spanes = movie.find_all("span")
            for span in spanes:
                print(span.text)
    else:
        print("오류 발생")


search_movie_poster("트랜스포머")