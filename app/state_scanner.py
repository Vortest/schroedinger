from app.page_parser import PageParser
from app.webelement import WebElement


class StateScanner(object):
    def __init__(self, driver):
        self.driver = driver
        self.page_parser = PageParser(self.driver)

    def check_state(self, state):
        self.get_live_elements()
        for element in state.elements:
            webelement = WebElement(self.driver,element.locators).element
            self.live_elements.remove(webelement)
        return self.live_elements

    def get_live_elements(self):
        self.live_elements = self.page_parser.get_all_elements()

    def get_diff(self, state):
        all_elements = state.elements
        self.get_live_elements()
        for element in state.elements:
            if element.element in self.live_elements:
                all_elements.remove(element)

        return len(all_elements) / len(state.elements)


#get all live elements
#for each saved element
#   check if the element is there
#   if it is:
#


#what do i want?
#i want a

