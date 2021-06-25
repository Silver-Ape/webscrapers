import string
from papers_with_code_scraper import PapersScraper


def newest_articles(json):
    with open('newest_articles.json', 'w') as outfile:
        outfile.write(json)


def main():

    urls = {'paperswithcode': 'https://paperswithcode.com/latest'}

    for i in urls.keys():
        if i == 'paperswithcode':
            paper = PapersScraper(urls['paperswithcode'])
            page_info = paper.pull_paper_info()
            newest_articles(page_info)


if __name__ == "__main__":
    main()
