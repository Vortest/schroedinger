import re
from selenium.webdriver.common.by import By
import sys
from attribute_builder import AttributeBuilder
import logging

class LocatorBuilder(object):

    def __init__(self, driver, element):
        self.driver = driver
        self.element = element
        self.builder = AttributeBuilder(element)
        self.attributes = self.builder.get_unique_attributes()
        self.locators = []

    def get_locators(self):
        for attribute in self.attributes:
            type = attribute[0]
            value = attribute[1]
            if type == "class":
                locator = (By.CLASS_NAME,value)
            elif type == "id":
                locator = (By.ID,value)
            elif type == "text":
                if self.element.tag_name == "a" and self.element.text != "":
                    locator = (By.LINK_TEXT,self.element.text)
                else:
                    locator = (By.XPATH,"//{}[contains(text(),'{}')]".format(self.element.tag_name,str(value)))
            elif type == "href":
                value = attribute[1].split('/')[-1]
                locator = (By.CSS_SELECTOR,"{}[{}*=\"{}\"]".format(self.element.tag_name, attribute[0], value))
            else:
                locator = (By.CSS_SELECTOR,"{}[{}*=\"{}\"]".format(self.element.tag_name, attribute[0], attribute[1]))
            if self.is_locator_valid(locator):
                self.locators.append(locator)

        if len(self.locators) == 0:
            try:
                logging.error("Could not get locators for element : {} found {} duplicate locators".format(self.element.html,len(self.builder.duplicate_attributes)))
            except:
                pass
                # self.get_complex_locators()
        return self.locators

    def is_locator_valid(self,locator):
        try:
            elements = self.driver.find_elements(locator[0],locator[1])
            if len(elements) == 1:
                return True
            else:
                logging.debug("Found %s elements with locator" % len(elements))
                return False
        except Exception as e:
            print "Unexpected error:", str(e)
            return False

    def get_complex_locators(self):
        css = self.element.tag_name
        for attribute in self.builder.duplicate_attributes:
            if attribute[0] != "text":
                css += ("[{}*={}]".format(attribute[0],attribute[1]))
        locator = (By.CSS_SELECTOR,css)
        if self.is_locator_valid(locator):
            self.locators.append(locator)