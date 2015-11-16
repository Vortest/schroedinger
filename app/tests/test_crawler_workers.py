import time
from app import state_builder
from app.state_crawler_worker import UrlCrawlerWorker, StateCrawlerWorker
from app.test_base import TestBase
from app.worker import Worker

class TestWorker(TestBase):
    def test_url_crawl(self):
        urlworker = UrlCrawlerWorker(1)
        urlworker.put("http://www.google.com/")
        urlworker.start()
        for i in range(1):
            print urlworker.get()
        urlworker.stop()


