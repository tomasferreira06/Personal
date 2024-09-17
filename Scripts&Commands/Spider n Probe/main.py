#https://en.wikipedia.org/wiki/Programmer

import requests
from bs4 import BeautifulSoup


def get_page(url):
    response = requests.get(url)


    soup = BeautifulSoup(response.content, 'html.parser')


    print(soup.find_all("a"))



get_page(input("\nWhat url would you like to scrape? "))