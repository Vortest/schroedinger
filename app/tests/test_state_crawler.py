from app.test_base import TestBase
from app.state_crawler import StateCrawler

class CrawlerTest(TestBase):
    def test_state_crawl(self):
        url = "http://www.google.com"
        crawl = StateCrawler(self.driver)
        state_id = crawl.crawl_url(url)
        print "State id is : %s" % state_id


    #
    #
    # def test_generate(self):
    #     url = "http://www.google.com/"
    #     self.driver.get(url)
    #     state_builder = StateBuilder(self.driver)
    #     initial_state = state_builder.get_current_state(self.driver)
    #     print "there are {} elemnets1 founds".format(len(initial_state.elements))
    #
    #     from app import element_filter
    #     text_fields = element_filter.filter_elements(initial_state.get_web_elements(self.driver),"input",("type","text"))
    #     submit_fields = element_filter.filter_elements(initial_state.get_web_elements(self.driver),"input",("type","submit"))
    #
    #     print "Found %s text field" % len(text_fields)
    #     for field in text_fields:
    #         field.highlight(1)
    #         field.send_keys("SOMETHING")
    #     new_state = state_builder.get_current_state(self.driver)
    #
    #     if new_state != initial_state:
    #         print "new state detected"
    #     else:
    #         for field in submit_fields:
    #             field.highlight()
    #             field.click()