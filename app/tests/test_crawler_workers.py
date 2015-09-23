import time
from app import state_builder
from app.state_crawler_worker import UrlCrawlerWorker, StateCrawlerWorker
from app.test_base import TestBase
from app.worker import Worker

class TestWorker(TestBase):
    def test_page_crawl(self):
        urlworker = UrlCrawlerWorker(1)
        urlworker.put("http://www.google.com/")
        urlworker.start()
        stateworker = StateCrawlerWorker(5)
        stateworker.start()
        stateworker.put(urlworker.get())
        for i in range(10):
            print stateworker.get()



