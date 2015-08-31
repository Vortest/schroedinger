from selenium.webdriver.common.by import By
from browser_manager import BrowserManager
import element_filter

class PageParser(object):

    def __init__(self,url):
        self.url = url

    def get_all_elements(self):
        BrowserManager.get_driver().get(self.url)
        eles = BrowserManager.get_driver().find_elements(By.CSS_SELECTOR,"*")
        visible_eles = element_filter.filter_visible_elements(eles)
        return visible_eles
