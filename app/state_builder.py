from models.element import Element
from webelement import WebElement
from locator_builder import LocatorBuilder
from page_parser import PageParser
from models.state import State


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
                new_element = Element(locators=locators)
                new_element.save()
                locator_elements.append(new_element)
                WebElement(self.driver,new_element.locators).highlight()
        state = State(elements=locator_elements,url=self.driver.current_url)
        state.save()
        state.get_html_info()
        return state