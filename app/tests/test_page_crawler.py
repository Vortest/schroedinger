from app.page_crawler import PageCrawler
from app.state_builder import StateBuilder
from app.test_base import TestBase
import app.config as config
from app.state_crawler import StateCrawler

class TestPageCrawler(TestBase):
    def test_page_crawl(self):
        url = "http://www.google.com"
        crawl = PageCrawler(self.driver)
        urls = crawl.get_links_on_url(url)

    def test_crawl(self):
        url = "http://www.google.com"
        crawl = PageCrawler(self.driver)
        urls = crawl.crawl_url(url)
        urls = sorted(urls, key=len)
        for url in urls:
            print url

