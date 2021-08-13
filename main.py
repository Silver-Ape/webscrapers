import string
from papers_with_code_scraper import PapersScraper
from arxiv_ml_scraper import arXivScraper
import json

# this is only for testing
def json_write(json_file):
    with open('newest_articles.json', 'w') as outfile:
        json.dump(json_file, outfile)
        outfile.close()


def main():

    urls = {'paperswithcode': 'https://paperswithcode.com/latest',
            # 'arxiv_AI': 'https://arxiv.org/list/cs.AI/pastweek?show=100',
            # 'arxiv_ML': 'https://arxiv.org/list/stat.ML/pastweek?show=100'
        }
    final_output = {}
    for i in urls.keys():
        if i == 'paperswithcode':
            paper = PapersScraper(urls['paperswithcode'])
            page_info = paper.pull_paper_info()
            final_output['paperswithcode'] = page_info
            print("paperswithcode done")
        # if i == 'arxiv_AI' or i == 'arxiv_ML':
        #     paper = arXivScraper(urls[i])
        #     page_info = paper.pull_paper_info()
        #     final_output['arXiv'] = page_info
        #     print("arxiv done")

    json_write(final_output)


if __name__ == "__main__":
    main()
