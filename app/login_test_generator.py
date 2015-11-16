from app import element_matcher
from app.page_parser import PageParser
from app import element_filter
from models.element_state import ElementType
from app.webelement import WebElement


class LoginTestGenerator(object):
    def __init__(self, driver, data = {}):
        self.driver = driver
        self.parser = PageParser(self.driver)
        self.data = data

    def _get_inputs(self):
        elements = self.parser.get_all_elements()
        inputs = element_filter.filter_inputs(elements)
        return inputs

    def _check_element(self, element):
        pass

    def _get_element_type(self, element):
        element_matcher.ElementTypes.LOGIN

    def generate(self):
        matcher = element_matcher.ElementMatcher()
        elements = self._get_inputs()
        for element in elements:
            type = matcher.match(element)
            if type == ElementType.LOGIN:
                WebElement(self.driver,element.locators).click()
            if type == ElementType.USERNAME:
                WebElement(self.driver,element.locators).send_keys(self.data[ElementType.USERNAME])
            if type == ElementType.PASSWORD:
                WebElement(self.driver,element.locators).send_keys(self.data[ElementType.PASSWORD])
            if type == ElementType.SUBMIT:
                WebElement(self.driver,element.locators).click()

