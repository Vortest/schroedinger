import re
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from app import element_filter


class PageCrawler(object):
    def __init__(self, driver, max_results=100):
        self.driver = driver
        self.max_results = max_results
        PageCrawler.all_urls = []

    all_urls = []

    def crawl_url(self, root_url):
        if len(PageCrawler.all_urls) >=self.max_results:
            return sorted(PageCrawler.all_urls)
        # print "Currently %s urls" % len(PageCrawler.all_urls)
        urls = self.get_links_on_url(root_url)
        new_urls = []
        for url in urls:
            if url is not None and url not in PageCrawler.all_urls and len(PageCrawler.all_urls) < self.max_results:
                # print "Found %s"  % url
                PageCrawler.all_urls.append(url)
                new_urls.append(url)
        # print "Found %s new URLS" % len(new_urls)
        if len(PageCrawler.all_urls) < self.max_results:
            for url in new_urls:
                domain = re.findall("\.(\w*)\.",str(url))
                if len(domain) == 0:
                    domain = re.findall("(\w*)\.",str(url))
                if len(domain) > 0:
                    if str(domain[0]) in self.driver.current_url:
                        self.crawl_url(url)
                    else:
                        print "wrong domain %s" % str(domain[0])

        return sorted(PageCrawler.all_urls)

    def get_links_on_url(self, url):
        self.driver.get(url)
        all_links = []
        links = self.driver.find_elements(By.PARTIAL_LINK_TEXT, "")
        links = element_filter.filter_visible_elements(links)
        for link in links:
            try:
                href = link.get_attribute("href")
                if href == "":
                    break
                all_links.append(href)
            except WebDriverException as e:
                pass
        print "Found %s links on %s" % (len(links), url)
        return sorted(all_links)


