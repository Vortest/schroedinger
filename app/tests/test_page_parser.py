from selenium.webdriver.common.by import By
from app import element_filter
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

    def test_all_elements_are_present(self):
        url = "http://www.google.com"
        self.driver.get(url)
        elements = PageParser(self.driver).get_all_elements()
        elements = element_filter.filter_tag(elements,"a")
        links = self.driver.find_elements(By.PARTIAL_LINK_TEXT,"")
        links = element_filter.filter_visible_elements(links)
        assert len(links) == len(elements)