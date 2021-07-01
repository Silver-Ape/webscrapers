from bs4 import BeautifulSoup
import requests


class PapersScraper:
    def __init__(self, url):
        self.url = url
        self.recent = []

    def get_recent(self):
        self._refresh_latest()
        return self.recent

    def _refresh_latest(self):
        try:
            if self.url != 'https://paperswithcode.com/latest':
                raise BrokenFormat

            addOns = []
            page = requests.get(self.url)
            soup = BeautifulSoup(page.text, 'html.parser')
            rows = soup.find_all('div', {"class": "row infinite-item item"})
            for children in rows:
                addOns.append(
                    'https://paperswithcode.com' + children.findChild("a")[
                        'href'])

            self.recent = addOns
            print('refreshed')

        except BrokenFormat:
            print("Incorrect link for function")

    def _paper_info(self, link):
        """
            Date ,authors ,publisher, title and number of citations
            :return:
        """

        page = requests.get(link)
        soup = BeautifulSoup(page.text, 'html.parser')
        author_span = soup.find_all('span', {"class": "author-span"})

        name = soup.find('h2').string.rstrip().lstrip()
        date = author_span[0].string
        authors = ''
        for i in range(1, len(author_span)):
            authors += author_span[i].string.lstrip().rstrip() + '/'

        paper_abstract = soup.find('div', {'class': 'paper-abstract'}).find('p').text.lstrip().rstrip().replace('read more', '')
        # paper_abstract += soup.find('div', {'class': 'paper-abstract'}).find('span', {'class': 'reverse-hidden-element'}).text.lstrip().rstrip()
        # print(paper_abstract)

        pdf = soup.find('div', {'class': 'paper-abstract'}).find('a', {"class": "badge badge-light"})['href']
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
        print(json_outputs)
        return json_outputs


# Exception Class
class BrokenFormat(Exception):
    pass
