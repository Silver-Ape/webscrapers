from bs4 import BeautifulSoup
import requests
import pandas as pd
import string


class PapersScraper:
    def __init__(self, url):
        self.url = url
        self.recent = []

    def get_latest(self):
        try:
            if self.url != 'https://paperswithcode.com/latest':
                raise BrokenFormat

            addOns = []
            page = requests.get(self.url)
            soup = BeautifulSoup(page.text, 'html.parser')
            rows = soup.find_all('div', {"class": "row infinite-item item"})
            for children in rows:
                addOns.append('https://paperswithcode.com' + children.findChild("a")['href'])
            print(addOns)

        except BrokenFormat:
            print("Incorrect link for function")


class BrokenFormat(Exception):
    pass
