from papers_with_code_scraper import PapersScraper

# testing PaperScraper
paper = PapersScraper('https://paperswithcode.com/latest')
latest_articles = paper.get_latest()
print(latest_articles)
