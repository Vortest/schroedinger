import time
from app import state_builder
from app.page_crawler_worker import PageCrawlerWorker
from app.state_bulder_worker import StateBuilderWorker
from app.test_base import TestBase
from app.worker import Worker

class TestWorker(TestBase):
    def test_one_worker(self):
        worker = StateBuilderWorker(5)
        worker.put("http://www.google.com")
        worker.start()
        worker.stop()
        state = worker.get()
        print state.url == u'https://www.google.com/?gws_rd=ssl'

    def test_multiple_workers(self):
        worker = StateBuilderWorker(5)
        worker.put("http://www.google.com")
        worker.put("http://www.google.com")
        worker.put("http://www.google.com")
        worker.put("http://www.google.com")
        worker.put("http://www.google.com")
        worker.put("http://www.google.com")
        worker.put("http://www.google.com")
        worker.put("http://www.google.com")
        worker.put("http://www.google.com")
        worker.put("http://www.google.com")
        worker.start()
        worker.stop()
        for i in range(10):
            state = worker.get()
            print state.url

    def test_page_crawl(self):
        worker = PageCrawlerWorker(5)
        worker.crawl_from_root("http://www.bluemodus.com/")
        worker.start()
        time.sleep(20)
        worker.stop()
        for i in range(10):
            url = worker.get()
            print url


