from selenium.webdriver.common.by import By
from app.webelement import WebElement
from app.state_builder import StateBuilder
from app.test_base import TestBase
from models.element import Locator


class StateTest(TestBase):
    def test_state_builder(self):
        self.url = "http://www.google.com/"
        self.driver.get(self.url)
        builder = StateBuilder(self.driver)
        state = builder.get_current_state()
        assert len(state.elements) >= 15

    def test_compare_same_page(self):
        self.url = "http://www.google.com/"
        self.driver.get(self.url)
        builder = StateBuilder(self.driver)
        state = builder.get_current_state()

        self.url2 = "http://www.google.com/"
        self.driver.get(self.url2)
        builder = StateBuilder(self.driver)
        state2 = builder.get_current_state()
        assert state == state2

    def test_compare_diff_page(self):
        self.url = "http://www.google.com/"
        self.driver.get(self.url)
        builder = StateBuilder(self.driver)
        state = builder.get_current_state()

        self.url2 = "http://www.bluemodus.com/"
        self.driver.get(self.url2)
        builder = StateBuilder(self.driver)
        state2 = builder.get_current_state()
        assert state != state2

    def test_compare_similar_pages(self):
        self.url = "http://www.google.com/"
        self.driver.get(self.url)
        builder = StateBuilder(self.driver)
        state = builder.get_current_state()

        self.url2 = "http://www.google.co.uk/"
        self.driver.get(self.url2)
        builder = StateBuilder(self.driver)
        state2 = builder.get_current_state()

        assert state != state2


    def test_subtract_state(self):
        self.url = "http://www.google.com/"
        self.driver.get(self.url)
        builder = StateBuilder(self.driver)
        state = builder.get_current_state()

        self.url2 = "http://www.google.co.uk/"
        self.driver.get(self.url2)
        builder = StateBuilder(self.driver)
        state2 = builder.get_current_state()

        uk_diff = state2 - state
        uk_diff.verify_state(self.driver)

    def test_divide_state(self):
        self.url = "http://www.google.com"
        self.driver.get(self.url)
        builder = StateBuilder(self.driver)
        state = builder.get_current_state()

        self.url2 = "http://www.google.co.uk"
        self.driver.get(self.url2)
        builder = StateBuilder(self.driver)
        state2 = builder.get_current_state()

        shared_state = state2 / state
        shared_state.verify_state(self.driver)

        self.driver.get("http://www.google.com/")
        shared_state.verify_state(self.driver)

    def test_verify_state(self):
        self.url = "http://www.google.com"
        self.driver.get(self.url)
        builder = StateBuilder(self.driver)
        state = builder.get_current_state()
        self.driver.get(self.url)
        state.verify_state(self.driver)

    def test_get_missing_elements(self):
        self.url = "http://www.google.com"
        self.driver.get(self.url)
        builder = StateBuilder(self.driver)
        state = builder.get_current_state()
        state.elements.append(WebElement(self.driver, [Locator(by=By.CSS_SELECTOR, value="INVALID")]))
        missing_elements = state.get_missing_elements(self.driver)
        assert len(missing_elements) == 1

    def test_remove_missing_elements(self):
        self.url = "http://www.google.com"
        self.driver.get(self.url)
        builder = StateBuilder(self.driver)
        state = builder.get_current_state()
        state.elements.append(WebElement(self.driver, [Locator(by=By.CSS_SELECTOR, value="INVALID")]))
        missing_elements = state.get_missing_elements(self.driver)
        for element in missing_elements:
            print "removing %s" % element
            state.remove_element(element)
            assert element not in state.elements

    def test_add_new_element(self):
        self.url = "http://www.google.com"
        self.driver.get(self.url)
        builder = StateBuilder(self.driver)
        state = builder.get_current_state()
        num_elements = len(state.elements)
        state.remove_element(state.elements[1])
        new_state = builder.get_current_state()
        diff_state = new_state - state
        assert len(diff_state.elements) == 1
        for element in diff_state.elements:
            state.add_element(element)

        state.verify_state(self.driver)

        assert len(state.elements) == num_elements








