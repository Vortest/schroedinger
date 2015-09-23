import re
from selenium.webdriver.common.by import By
import sys
from attribute_builder import AttributeBuilder
import logging
from models.element_state import Locator

logger = logging.getLogger()

class LocatorBuilder(object):

    def __init__(self, driver, element):
        self.driver = driver
        self.element = element
        self.builder = AttributeBuilder(element)
        self.attributes = self.builder.get_unique_attributes()
        self.locators = []

    def get_locators(self):
        for attribute in self.attributes:
            self.get_locators_for_attribute(attribute)
        if len(self.locators) == 0:
            try:
                for att in self.builder.duplicate_attributes:
                    self.get_locators_for_attribute(att)
                if len(self.locators) == 0:
                    logging.error("Could not get locators for element : {} found {} duplicate attributes".format(self.builder.html,len(self.builder.duplicate_attributes)))
            finally:
                self.get_complex_locators()
        return self.locators

    def get_locators_for_attribute(self, attribute):
        type = attribute[0]
        value = attribute[1]
        if type == "" or value == "":
            return
        if type == "class":
            locator = Locator(by=By.CLASS_NAME,value=value)
        elif type == "id":
            locator = Locator(by=By.ID,value=value)
        elif type == "text":
            if self.element.tag_name == "a" and self.element.text != "":
                locator = Locator(by=By.LINK_TEXT,value=self.element.text)
            else:
                if "'" in str(value):
                    locator = Locator(by=By.XPATH,value="//{}[contains(text(),\"{}\")]".format(self.element.tag_name,str(value)))
                else:
                    locator = Locator(by=By.XPATH,value="//{}[contains(text(),'{}')]".format(self.element.tag_name,str(value)))
        elif type == "href":
            value = attribute[1].split('//')[-1]
            value = value.split('?')[0]
            value = value.split('&')
            locator = Locator(by=By.CSS_SELECTOR,value="{}[{}*=\"{}\"]".format(self.element.tag_name, attribute[0], value))
        else:
            locator = Locator(by=By.CSS_SELECTOR,value="{}[{}*=\"{}\"]".format(self.element.tag_name, attribute[0], attribute[1]))
        if self.is_locator_valid(locator):
            self.locators.append(locator)

    def is_locator_valid(self,locator):
        try:
            elements = self.driver.find_elements(locator.by,locator.value)
            if len(elements) == 1:
                if self.element != elements[0]:
                    logging.error("Wrong element matched")
                    return False
                else:
                    return True
            else:
                logging.info("Found %s elements with locator" % len(elements))
                for element in elements:
                    logging.debug(element.html)
                return False
        except Exception as e:
            logging.error("is_locator_valid failed : %s " % str(e))
            return False

    def get_ancestor_locators(self):
        return
        parent = self.element.find_parent()
        # parent_builder = LocatorBuilder(self.driver, parent)
        # parent_locators = parent_builder.get_locators()
        # for parent_locator in parent_locators:
        #     for locator in self.builder:
        #     "%s>%s" % (parent_locator[1],)
        # new_locator = (By.CSS_SELECTOR,"")




    def get_complex_locators(self):
        return
        logging.info("Creating complex locators")
        css = self.element.tag_name
        for attribute in self.builder.get_attributes():
            if attribute[0] != "text":
                css += ("[{}*={}]".format(attribute[0],attribute[1]))
        locator = Locator(by=By.XPATH,value=css)
        logging.info("Trying locator %s" % css)
        if self.is_locator_valid(locator):
            self.locators.append(locator)