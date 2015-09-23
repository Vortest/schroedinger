from selenium.webdriver.common.by import By
from app import state_builder
from app.test_base import TestBase
from app.webelement import WebElement
from models.element_state import ElementState, Locator


class TestElementCompare(TestBase):
    def test_compare_same_element(self):
        self.driver.get("http://www.google.com/")
        state = state_builder.get_current_state(self.driver)
        element1 = state.elements[0]
        element2 = state.elements[0]
        from app.element_comparer import ElementComparer
        result = ElementComparer(self.driver).compare_elements(element1,element2)
        assert result == 0

    def test_compare_diff_element(self):
        self.driver.get("http://www.google.com/")
        state = state_builder.get_current_state(self.driver)
        element1 = state.elements[0]
        element2 = state.elements[1]
        from app.element_comparer import ElementComparer
        result = ElementComparer(self.driver).compare_elements(element1,element2)
        assert result != 0, result
        print result

    def test_compare_similar_element(self):
        self.driver.get("http://www.google.com/")
        state = state_builder.get_current_state(self.driver)
        element1 = state.elements[0]
        element2 = state.elements[1]
        from app.element_comparer import ElementComparer
        result = ElementComparer(self.driver).compare_elements(element1,element2)
        assert result != 0, result
        print result


