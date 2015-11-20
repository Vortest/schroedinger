import unittest
from models.crawler_task import CrawlerTask
from models.state import State
from models.suite import Suite
import datetime

class TestQueue(unittest.TestCase):

    def test_queue(self):
        queue = CrawlerTask(status=CrawlerTask.Status.FAILED, message="This is a message", user="12345", url="http://www.google.com/")
        queue.save()

    def test_get_queue(self):
        queue = CrawlerTask.objects(start_after__lte=datetime.datetime.now(), status=CrawlerTask.Status.QUEUED)
