import string
from papers_with_code_scraper import PapersScraper
import json


def json_write(json_file):
    with open('newest_articles.json', 'w') as outfile:
        json.dump(json_file, outfile)
        outfile.close()


def main():

    urls = {'paperswithcode': 'https://paperswithcode.com/latest'}
    final_output = {}
    for i in urls.keys():
        if i == 'paperswithcode':
            paper = PapersScraper(urls['paperswithcode'])
            page_info = paper.pull_paper_info()
            final_output['paperswithcode'] = page_info
    json_write(final_output)

if __name__ == "__main__":
    main()
