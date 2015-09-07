from element import Element
from locator_builder import LocatorBuilder
from page_parser import PageParser
from state import State


class StateBuilder(object):
    def __init__(self, driver):
        self.driver = driver
        self.parser = PageParser(self.driver)

    def get_current_state(self):
        locator_elements = []
        elements = self.parser.get_all_elements()
        for element in elements:
            builder = LocatorBuilder(self.driver, element)
            locators = builder.get_locators()
            if(len(locators)) > 0:
                new_element = Element(self.driver,locators)
                locator_elements.append(new_element)
        state = State(locator_elements,self.driver.current_url)
        return state