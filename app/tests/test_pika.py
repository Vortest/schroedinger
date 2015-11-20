import unittest
import pika

class TestPika(unittest.TestCase):
    def test_producer(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters(
               host='localhost'))
        channel = connection.channel()
        channel.queue_declare(queue="hello")
        channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
        print " [x] Sent 'Hello World!'"
        connection.close()

    def test_consumer(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters(
            host='localhost'))
        channel = connection.channel()

        channel.queue_declare(queue='hello')

        print ' [*] Waiting for messages. To exit press CTRL+C'

        def callback(ch, method, properties, body):
            print " [x] Received %r" % (body,)

        channel.basic_consume(callback,
                              queue='hello',
                              no_ack=True)

        channel.start_consuming()
        channel.stop_consuming()
