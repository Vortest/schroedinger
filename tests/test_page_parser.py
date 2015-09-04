from app.test_base import TestBase
from app.page_parser import PageParser


class TestPageParser(TestBase):

    urls = ["http://www.google.com",
            "http://www.bluemodus.com",
            "http://www.galvanize.com",
            "http://www.grubhub.com",
            "http://www.percolate.com"]


    def test_parse_page(self):
        for url in self.urls:
            try:
                self.driver.get(url)
                elements = PageParser(self.driver).get_all_elements()
                print "Found {} elements on {}".format(len(elements), url)
            except Exception as e:
                print str(e)
