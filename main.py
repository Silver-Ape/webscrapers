import string
from papers_with_code_scraper import PapersScraper


def main():

    urls = {'paperswithcode': 'https://paperswithcode.com/latest'}

    for i in urls.keys():
        if i == 'paperswithcode':
            paper = PapersScraper(urls['paperswithcode'])
            latest_articles = paper.get_latest()
            print(latest_articles)



# if __name__ == "__main__":
#     print(main())
