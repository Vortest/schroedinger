from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement as webdriverElement
import logging
import time
import images

class WrappedWebElement(webdriverElement):
    @property
    def element(self):
        if isinstance(self._element, webdriverElement):
            return self._element
        else:
            return self._element.element

    @property
    def driver(self):
        return self._driver

    def __repr__(self):
        return self.html

    def __init__(self, element):
        self._element = element
        self._driver = element.parent

    def __eq__(self, other):
        try:
            return self.location == other.location
        except Exception as e:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def is_stale(self):
        try:
            self.element.is_enabled()
            return False
        except Exception as e:
            return True

    def find_element(self, by=By.ID, value=None):
        ele = self.element.find_element(by, value)
        if isinstance(ele,WrappedWebElement):
            return ele
        else:
            return WrappedWebElement(ele)

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
        try:
            new_image = images.get_element_image(self.driver, self.element)
            base_64_image = images.get_base64_from_image(new_image)
            return base_64_image
        except Exception as e:
            logging.exception("Could not capture element screenshot : " + str(e))
            return ""

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
        elements =  self.element.find_elements(by, value)
        new_eles = map(self.wrap_element,elements)
        return new_eles

    def wrap_element(self,element):
        return WrappedWebElement(element)

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
        image = images.get_element_image(self.driver, self.element)
        image.save(filename)

    @property
    def text(self):
        return self.element.text.decode('utf-8')

    def is_selected(self):
        return self.element.is_selected()

    def location_once_scrolled_into_view(self):
        return self.element.location_once_scrolled_into_view()

    @property
    def screenshot_as_png(self):
        new_image = images.get_element_image(self.driver, self.element)
        return new_image

    def send_keys(self, *value):
        self.element.send_keys(*value)
        # logging.debug("SendKeys %s" % value)

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

    def highlight(self,length=.1,color="yellow"):
        background = self.driver.execute_script("return arguments[0].style.background", self.element)
        self.driver.execute_script("arguments[0].style.background='%s'; return;" % color,self.element)
        if length == -1:
            return
        time.sleep(length)
        self.driver.execute_script("arguments[0].style.background='%s'; return;" % background,self.element)

    @property
    def html(self):
        if "<" in self.inner_html:
            html =  (self.outer_html.replace(self.inner_html,"")).encode('utf-8')
        else:
            html = (self.outer_html).encode('ascii','ignore')
        return (html).encode('ascii','ignore')

    @property
    def inner_html(self):
        html = self.element.get_attribute(('innerHTML'))
        return (html).encode('ascii','ignore')

    @property
    def outer_html(self):
        html = self.element.get_attribute('outerHTML')
        return (html).encode('ascii','ignore')

    @property
    def value(self):
        value = self.element.get_attribute("value")
        return (value).encode('ascii','ignore')

    def find_parent(self):
        return self.find_element(By.XPATH,"..")

    def find_child(self):
        return self.find_element(By.CSS_SELECTOR,">")

    @property
    def area(self):
        return self.size["height"] * self.size["height"]

    def is_editable(self):
        tags = ["input","textarea"]
        return self.tag_name in tags

    def is_clickable(self):
        tags = ["a","button"]
        return self.tag_name in tags