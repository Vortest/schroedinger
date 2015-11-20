import datetime
import threading
import pika
from models.crawler_task import CrawlerTask


class CrawlerProducer():
    QUEUE = "crawl"
    HOST = "localhost"

    def __init__(self, num_threads):
        self.num_threads = num_threads
        self.Pool = []

    def process_queue(self):
        while self.flag !='stop':
            connection = pika.BlockingConnection(pika.ConnectionParameters(
               host=CrawlerProducer.HOST))
            channel = connection.channel()
            channel.queue_declare(queue=CrawlerProducer.QUEUE)
            tasks = CrawlerTask.objects(start_after__lte=datetime.datetime.now(), status=CrawlerTask.Status.QUEUED)
            for task in tasks:
                print "Found a crawl item in the DB: %s %s" % (task.url, task.id)
                task.status=CrawlerTask.Status.IN_PROGRESS
                task.save()
                channel.basic_publish(exchange='',
                      routing_key=CrawlerProducer.QUEUE,
                      body=str(task.id))
                print " [x] Sent '%s" % task.id
            connection.close()


    def start(self):
        self.flag = 'start'
        for i in range(self.num_threads):
             thread = threading.Thread(target=self.process_queue)
             thread.start()
             self.Pool.append(thread)

    def stop(self):
        self.flag == 'stop'
        while self.Pool:
            datetime.time.sleep(1)
            for index,the_thread in enumerate(self.Pool):
                if the_thread.isAlive():
                    continue
                else:
                    del self.Pool[index]
                break
