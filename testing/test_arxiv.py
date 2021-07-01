from arxiv_ml_scraper import arXivScraper


def test_arxiv_refresh_latest():
    paper = arXivScraper('https://arxiv.org/list/cs.AI/pastweek?show=100')
    paper._refresh_latest()
    print(paper.get_recent())


# testing arXivScraper._paper_info()
def test_arxiv_paper_info():
    paper = arXivScraper('https://arxiv.org/list/cs.AI/pastweek?show=100')
    paper._refresh_latest()
    paper._paper_info(
        'https://arxiv.org/abs/2106.16176')


# testing arXivScraper.pull_paper_info
def test_paperscraper_pull_paper_info():
    paper = arXivScraper('https://arxiv.org/list/cs.AI/pastweek?show=100')
    # print()
    paper.pull_paper_info()


if __name__ == '__main__':
    # test_arxiv_refresh_latest()
    # test_arxiv_paper_info()
    test_paperscraper_pull_paper_info()
