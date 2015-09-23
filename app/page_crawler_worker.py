import abc
import threading,Queue,time,sys,traceback
import re
from app import browser_manager
from app import state_builder
from app.worker import Worker
from threading import Thread, current_thread, currentThread
from app import browser_launcher
from app import page_crawler

class PageCrawlerWorker(Worker):

    def __init__(self, num_threads, max_results= 100):
        super(Worker,self).__init__()
        self.all_urls = []
        self.num_threads = num_threads
        self.num_threads = num_threads
        self.Qin  = Queue.Queue()
        self.Qout = Queue.Queue()
        self.Qerr = Queue.Queue()
        self.Pool = []
        self.max_results = max_results

    def process_item(self, root_url):
        print "Crawling %s %s" % (currentThread(),root_url)
        driver = browser_launcher.launch_browser()
        print "Driver launched"
        urls = page_crawler.PageCrawler(driver).get_links_on_url(root_url)
        print "crawling complete"
        driver.quit()
        print "driver quit"
        for url in urls:
            print "appending %s" % url
            self.put(url)
        return urls

    def crawl_from_root(self, url):
        print "Crawling from root %s" % url
        self.root_url = url
        self.put(url)
        print "Crawl complete"

    def put(self,url,flag='ok'):
        print "there are %s urls" % len(self.all_urls)
        if len(self.all_urls) >= self.max_results:
            print "max results found"
        if url in self.all_urls:
            print "url already found %s" % url
        else:
            self.all_urls.append(url)
            domain = re.findall("\.(\w*)\.",str(url))
            if "mailto:" not in url:
                if len(domain) == 0:
                    domain = re.findall("(\w*)\.",str(url))
                if len(domain) > 0:
                    if str(domain[0]) in self.root_url:
                        print "Adding %s to the queue" % url
                        self.Qin.put([flag,url])
                    else:
                        print "wrong domain %s" % str(domain[0])
