from bs4 import BeautifulSoup


class BaseScraper:
    def __init__(self, url):
        self.url = url
        self.recent = []

    def get_recent(self):
        pass

    def pull_paper_info(self):
        pass
