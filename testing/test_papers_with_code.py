from papers_with_code_scraper import PapersScraper


# testing PaperScraper.refresh_latest()
def test_paperscraper_refresh_latest():
    paper = PapersScraper('https://paperswithcode.com/latest')
    paper._refresh_latest()
    print(paper.get_recent())


# testing PaperScraper._paper_info()
def test_paperscraper_paper_info():
    paper = PapersScraper('https://paperswithcode.com/latest')
    paper._refresh_latest()
    paper._paper_info(
        'https://paperswithcode.com/paper/a-probabilistic-representation-of-dnns')


# testing PaperScraper.pull_paper_info
def test_paperscraper_pull_paper_info():
    paper = PapersScraper('https://paperswithcode.com/latest')
    # print()
    paper.pull_paper_info()


if __name__ == '__main__':
    # test_paperscraper_refresh_latest()
    test_paperscraper_paper_info()
    # test_paperscraper_pull_paper_info()
