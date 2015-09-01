from selenium.webdriver.common.by import By
from test_base import TestBase
from page_parser import PageParser
from attribute_builder import AttributeBuilder
import time


class TestAttributeBuilder(TestBase):
    def test_attribute_builder(self):
        self.driver.get("http://www.google.com/")
        time.sleep(1)
        element = self.driver.find_element(By.NAME,"q")
        builder = AttributeBuilder(element)
        attributes = builder.get_attributes()
        print "text is : " + element.text
        print attributes

    def test_attribute_builder_with_parent_item(self):
        self.driver.get("http://www.google.com/")
        time.sleep(1)
        element = self.driver.find_element(By.ID,"sbtc")
        print "testing item : "+ element.html
        builder = AttributeBuilder(element)
        attributes = builder.get_attributes()
        print attributes

    def test_get_unique_attributes(self):
        self.driver.get("http://www.google.com/")
        element = self.driver.find_element(By.NAME,"q")
        print "Testing element with html : %s" % element.html
        builder = AttributeBuilder(element)
        attributes = builder.get_unique_attributes()
        print attributes

    def test_get_unique_attributes_two(self):
        self.driver.get("http://www.google.com/")
        element = self.driver.find_element(By.LINK_TEXT,"Sign in")
        print "Testing element with html : %s" % element.html
        builder = AttributeBuilder(element)
        attributes = builder.get_unique_attributes()
        print attributes
