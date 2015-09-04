from selenium.webdriver.common.by import By

import element_filter


class PageParser(object):

    def __init__(self,driver):
        self.driver = driver
        html = self.driver.page_source


    def get_all_elements(self):
        eles = self.driver.find_elements(By.CSS_SELECTOR,"*")
        visible_eles = element_filter.filter_visible_elements(eles)
        final_elements = element_filter.filter_no_children(visible_eles)
        return final_elements
