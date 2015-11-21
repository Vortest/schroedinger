import unittest
import datetime
import pika
from app.crawler_consumer import CrawlerConsumer
from app.crawler_producer import CrawlerProducer
from models.crawler_task import CrawlerTask
import logging

pika_logger = logging.getLogger('pika')
pika_logger.setLevel(logging.CRITICAL)

class TestCrawlerQueue(unittest.TestCase):
    def test_crawler(self):
        task1 = CrawlerTask(status=CrawlerTask.Status.QUEUED, message="This is a message", user="12345", url="http://www.google.com/")
        task1.save()
        task2 = CrawlerTask(status=CrawlerTask.Status.FAILED, message="This is a message", user="12345", url="http://www.failed.com/")
        task2.save()
        task3 = CrawlerTask(status=CrawlerTask.Status.QUEUED, message="This is a message", user="12345", url="http://www.baidu.com/", start_after = datetime.datetime.now() + datetime.timedelta(seconds=10))
        task3.save()
        producer = CrawlerProducer(1)
        consumer = CrawlerConsumer()

        # producer.start()
        # producer.stop()