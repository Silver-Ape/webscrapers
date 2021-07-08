from bs4 import BeautifulSoup
import requests
from scraper_base import BaseScraper
from exceptions import BrokenFormat


class arXivScraper(BaseScraper):

    def __init__(self, url):
        super().__init__(url)
        # self.url = url
        # self.recent = []

    def get_recent(self):
        self._refresh_latest()
        return self.recent

    def _refresh_latest(self):
        try:
            if self.url != 'https://arxiv.org/list/cs.AI/pastweek?show=100' and self.url != 'https://arxiv.org/list/stat.ML/pastweek?show=100':
                print(self.url)
                raise BrokenFormat

            addOns = []
            page = requests.get(self.url)
            soup = BeautifulSoup(page.text, 'html.parser')
            rows = soup.find('div', {"id": "dlpage"}).find('dl').find_all('dt')
            for children in rows:
                addOns.append(
                    'https://arxiv.org/' +
                    children.find('span', {'class': 'list-identifier'}).find(
                        'a')['href'])
                # print('https://arxiv.org/' + children.find('span', {'class': 'list-identifier'}).find('a')['href'])
            self.recent = addOns
            print('refreshed')

        except BrokenFormat:
            print("Incorrect link for function")

    def _paper_info(self, link):
        page = requests.get(link)
        soup = BeautifulSoup(page.text, 'html.parser')

        author_span = soup.find_all('div', {"class": "authors"})[0].find_all(
            'a')
        authors = ''
        for i in author_span:
            authors += i.string + '/'

        name = soup.find('h1', {"class": "title mathjax"}).text.lstrip("Title:")
        date = soup.find('div', {'class': "dateline"}).string.lstrip().rstrip(']')[14:]
        paper_abstract = soup.find('blockquote', {"class": "abstract mathjax"}).text[len('Abstract:   '):]
        pdf = 'https://arxiv.org/' + soup.find('a', {"class": "abs-button download-pdf"})['href']

        return {
            'name': name,
            'date': date,
            'authors': authors,
            'abstract': paper_abstract,
            'pdf': pdf
        }

    def pull_paper_info(self):
        self._refresh_latest()
        json_outputs = {}
        for link in self.get_recent():
            info = self._paper_info(link)
            json_outputs[link] = info
        # print(json_outputs)
        return json_outputs
