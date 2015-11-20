import pika
from app import browser_launcher
from app import state_builder, action_builder
from models.crawler_task import CrawlerTask

class CrawlerConsumer():

    def consume_task(self):
        print "Consuming"
        connection = pika.BlockingConnection(pika.ConnectionParameters(
                host='localhost'))
        channel = connection.channel()

        channel.queue_declare(queue='crawl')

        print ' [*] Waiting for messages. To exit press CTRL+C'

        channel.basic_consume(self.callback,
                              queue='crawl',
                              no_ack=True)

        channel.start_consuming()

    def callback(self, ch, method, properties, body):
        print "Consumer Received ID : %r" % (body,)
        self.process_item(body)

    def process_item(self, id):
        print "Processing %s" % (id)
        task = CrawlerTask.objects.get(id=id)
        self.driver = browser_launcher.launch_browser()
        state =  self.crawl_url(task.url)
        print "Found %s elements" % state.elements
        self.driver.quit()
        print "UrlCrawler finished processing %s" % task.url
        task.status = CrawlerTask.Status.COMPLETED
        task.save()
        return state

    def crawl_url(self, url):
        print "Crawling URL " + url
        self.driver.get(url)
        initial_state = state_builder.get_current_state(self.driver)
        initial_state.save()
        blank_state = state_builder.get_blank_state()
        blank_state.save()
        nav_action = action_builder.get_nav_action(url,initial_state)
        nav_action.save()
        initial_state.init_actions = [nav_action]
        initial_state.save()
        print "Saved initial state %s" % initial_state.id
        return initial_state