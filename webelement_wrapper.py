from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import logging
import time

class WebElement(WebElement):
    @property
    def element(self):
        return self._element

    @property
    def driver(self):
        return self._driver

    def __init__(self, element):
        self._element = element
        self._driver = element.parent

    def is_stale(self):
        try:
            self.element.enabled
        except:
            return True

    def find_element(self, by=By.ID, value=None):
        return self.element.find_element(by, value)

    def find_element_by_xpath(self, xpath):
        return self.element.find_element_by_xpath(xpath)

    def find_elements_by_partial_link_text(self, link_text):
        return self.element.find_elements_by_partial_link_text(link_text)

    def get_attribute(self, name):
        return self.element.get_attribute(name)

    def find_element_by_name(self, name):
        return self.element.find_element_by_name(name)

    @property
    def screenshot_as_base64(self):
        return self.element.screenshot_as_base64()

    def is_enabled(self):
        return self.element.is_enabled()

    def find_element_by_css_selector(self, css_selector):
        return self.element.find_element_by_css_selector(css_selector)

    @property
    def size(self):
        return self.element.size

    def find_elements_by_tag_name(self, name):
        return self.element.find_elements_by_tag_name(name)

    def find_elements(self, by=By.ID, value=None):
        return self.element.find_elements(by, value)

    @property
    def rect(self):
        return self.element.rect

    @property
    def tag_name(self):
        return self.element.tag_name

    @property
    def parent(self):
        return self.element.parent

    def find_elements_by_class_name(self, name):
        return self.element.find_elements_by_class_name(name)

    def find_elements_by_name(self, name):
        return self.element.find_elements_by_name(name)

    def find_elements_by_id(self, id_):
        return self.element.find_elements_by_id(id_)

    def find_element_by_partial_link_text(self, link_text):
        return self.element.find_element_by_partial_link_text(link_text)

    def find_elements_by_link_text(self, link_text):
        return self.element.find_elements_by_link_text(link_text)

    def submit(self):
        self.element.submit()

    def is_displayed(self):
        return self.element.is_displayed()

    def screenshot(self, filename):
        return self.element.screenshot(filename)

    @property
    def text(self):
        return self.element.text

    def is_selected(self):
        return self.element.is_selected()

    def location_once_scrolled_into_view(self):
        return self.element.location_once_scrolled_into_view()

    @property
    def screenshot_as_png(self):
        return self.element.screenshot_as_png

    def send_keys(self, *value):
        logging.debug("SendKeys %s" % value)
        self.element.send_keys(value)

    def find_element_by_link_text(self, link_text):
        return self.element.find_element_by_link_text(link_text)


    def clear(self):
        self.element.clear()

    def find_element_by_id(self, id_):
        return self.element.find_element_by_id(id_)

    def find_element_by_class_name(self, name):
        return self.element.find_element_by_class_name(name)

    def _upload(self, filename):
        return self.element._upload(filename)

    def click(self):
        logging.debug("Clicking")
        self.element.click()

    def find_elements_by_xpath(self, xpath):
        return self.element.find_elements_by_xpath(xpath)

    @property
    def location(self):
        return self.element.location

    def value_of_css_property(self, property_name):
        return self.element.value_of_css_property(property_name)

    def find_element_by_tag_name(self, name):
        return self.element.find_element_by_tag_name(name)

    def find_elements_by_css_selector(self, css_selector):
        return self.element.find_elements_by_css_selector(css_selector)

    def highlight(self,length=.1):
        element = self.element
        background = self.driver.execute_script("return arguments[0].style.background", self.element)
        self.driver.execute_script("arguments[0].style.background='yellow'; return;",self.element)
        time.sleep(length)
        self.driver.execute_script("arguments[0].style.background='%s'; return;" % background,self.element)

    @property
    def html(self):
        if "<" in self.inner_html:
            html =  self.outer_html.replace(self.inner_html,"")
        else:
            html = self.outer_html
        return html

    @property
    def inner_html(self):
        html = self.element.get_attribute(('innerHTML'))
        return html

    @property
    def outer_html(self):
        html = self.element.get_attribute('outerHTML')
        return html