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
        return final_elements[:50]

    def get_usual_elements(self):
        all_links = []
        links = self.driver.find_elements(By.TAG_NAME,"a")
        buttons = self.driver.find_elements(By.TAG_NAME,'button')
        inputs = self.driver.find_elements(By.TAG_NAME,'input')
        images = self.driver.find_elements(By.TAG_NAME,'img')
        selects = self.driver.find_elements(By.TAG_NAME,'select')
        forms =  self.driver.find_elements(By.TAG_NAME,'form')
        all_links.extend(links)
        all_links.extend(buttons)
        all_links.extend(inputs)
        all_links.extend(images)
        all_links.extend(selects)
        all_links.extend(forms)
        visible_eles = element_filter.filter_visible_elements(all_links)
        final_elements = sorted(visible_eles,key=lambda element: element.area,reverse=True)
        return final_elements

