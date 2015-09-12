from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import logging
from wrapped_webelement import WrappedWebElement


class WebDriver():
    
    @property
    def driver(self):
        return self._driver
        
    def __init__(self,driver):
        self._driver = driver
    
    def find_element(self, by=By.ID, value=None):
        logging.debug("Finding WrappedWebElement %s %s" % (by, value))
        ele = WrappedWebElement(self.driver.find_element(by, value))
        #ele.highlight()
        return ele

    def find_elements(self, by=By.ID, value=None):
        logging.debug("Finding Elements %s %s" % (by, value))
        eles = self.driver.find_elements(by, value)
        new_eles = map(self.wrap_element,eles)
        #new_eles = map(self.highlight,new_eles)
        return new_eles

    def highlight(self, element, time=-1):
        element.highlight(time)
        return element

    def wrap_element(self,element):
        return WrappedWebElement(element)

    def find_element_by_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    def stop_client(self):
        self.driver.stop_client()

    def _unwrap_value(self, value):
        return self.driver._unwrap_value(value)

    def start_client(self):
        self.driver.start_client()

    def maximize_window(self):
        self.driver.maximize_window()

    def find_element_by_name(self, name):
        return self.driver.find_element_by_name(name)

    def implicitly_wait(self, time_to_wait):
        self.driver.implicitly_wait(time_to_wait)

    def get_cookie(self, name):
        return self.driver.get_cookie(name)

    def set_window_position(self, x, y, windowHandle='current'):
        self.driver.set_window_position(x, y, windowHandle)

    def switch_to_active_element(self):
        return self.driver.switch_to_active_element()

    def back(self):
        self.driver.back()

    def find_elements_by_name(self, name):
        return self.driver.find_elements_by_name(name)

    def start_session(self, desired_capabilities, browser_profile=None):
        self.driver.start_session(desired_capabilities, browser_profile)

    @property
    def current_url(self):
        return self.driver.current_url

    def get_window_size(self, windowHandle='current'):
        return self.driver.get_window_size(windowHandle)

    def find_elements_by_link_text(self, text):
        return self.driver.find_elements_by_link_text(text)

    def create_web_element(self, element_id):
        return self.driver.create_web_element(element_id)

    def file_detector(self, detector):
        return self.driver.file_detector(detector)

    def get_screenshot_as_file(self, filename):
        return self.driver.get_screenshot_as_file(filename)

    def delete_all_cookies(self):
        self.driver.delete_all_cookies()

    def desired_capabilities(self):
        return self.driver.desired_capabilities()

    def get_screenshot_as_png(self):
        return self.driver.get_screenshot_as_png()

    def switch_to(self):
        return self.driver.switch_to()

    def switch_to_window(self, window_name):
        self.driver.switch_to_window(window_name)

    def delete_cookie(self, name):
        self.driver.delete_cookie(name)

    def name(self):
        return self.driver.name()

    def title(self):
        return self.driver.title()

    def window_handles(self):
        return self.driver.window_handles()

    def find_element_by_id(self, id_):
        return self.driver.find_element_by_id(id_)

    def quit(self):
        self.driver.quit()

    def log_types(self):
        return self.driver.log_types()

    def get_window_position(self, windowHandle='current'):
        return self.driver.get_window_position(windowHandle)

    def find_element_by_tag_name(self, name):
        return self.driver.find_element_by_tag_name(name)

    def mobile(self):
        return self.driver.mobile()

    def find_elements_by_partial_link_text(self, link_text):
        return self.driver.find_elements_by_partial_link_text(link_text)

    def switch_to_alert(self):
        return self.driver.switch_to_alert()

    def switch_to_frame(self, frame_reference):
        self.driver.switch_to_frame(frame_reference)

    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)

    def find_element_by_css_selector(self, css_selector):
        return self.driver.find_element_by_css_selector(css_selector)

    def get_log(self, log_type):
        return self.driver.get_log(log_type)

    def _wrap_value(self, value):
        return self.driver._wrap_value(value)

    def set_window_size(self, width, height, windowHandle='current'):
        self.driver.set_window_size(width, height, windowHandle)

    def find_elements_by_tag_name(self, name):
        return self.driver.find_elements_by_tag_name(name)

    def find_elements_by_class_name(self, name):
        return self.driver.find_elements_by_class_name(name)

    def find_elements_by_id(self, id_):
        return self.driver.find_elements_by_id(id_)

    def execute_async_script(self, script, *args):
        return self.driver.execute_async_script(script, *args)

    def set_page_load_timeout(self, time_to_wait):
        self.driver.set_page_load_timeout(time_to_wait)

    def find_element_by_partial_link_text(self, link_text):
        return self.driver.find_element_by_partial_link_text(link_text)

    def get(self, url):
        self.driver.get(url)

    def execute(self, driver_command, params=None):
        return self.driver.execute(driver_command, params)

    def orientation(self, value):
        return self.driver.orientation(value)

    def refresh(self):
        self.driver.refresh()

    def set_script_timeout(self, time_to_wait):
        self.driver.set_script_timeout(time_to_wait)

    def application_cache(self):
        return self.driver.application_cache()

    def forward(self):
        self.driver.forward()

    @property
    def current_window_handle(self):
        return self.driver.current_window_handle

    def find_element_by_link_text(self, link_text):
        return self.driver.find_element_by_link_text(link_text)

    def get_cookies(self):
        return self.driver.get_cookies()

    def switch_to_default_content(self):
        self.driver.switch_to_default_content()

    def close(self):
        self.driver.close()

    def find_element_by_class_name(self, name):
        return self.driver.find_element_by_class_name(name)

    @property
    def page_source(self):
        return self.driver.page_source

    def add_cookie(self, cookie_dict):
        self.driver.add_cookie(cookie_dict)

    def get_screenshot_as_base64(self):
        return self.driver.get_screenshot_as_base64()

    def find_elements_by_xpath(self, xpath):
        return self.driver.find_elements_by_xpath(xpath)

    def find_elements_by_css_selector(self, css_selector):
        return self.driver.find_elements_by_css_selector(css_selector)

    @property
    def html(self):
        return self.driver.page_source