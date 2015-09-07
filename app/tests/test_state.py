from selenium.webdriver.common.by import By
from app.element import Element
from app.state_builder import StateBuilder
from app.test_base import TestBase

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
        assert len(uk_diff.elements) > 0

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
        shared_state.verify_state()

        self.driver.get("http://www.google.com/")
        shared_state.verify_state()

    def test_verify_state(self):
        self.url = "http://www.google.com"
        self.driver.get(self.url)
        builder = StateBuilder(self.driver)
        state = builder.get_current_state()
        self.driver.get(self.url)
        state.verify_state()

    def test_get_missing_elements(self):
        self.url = "http://www.google.com"
        self.driver.get(self.url)
        builder = StateBuilder(self.driver)
        state = builder.get_current_state()
        state.elements.append(Element(self.driver, [(By.CSS_SELECTOR, "INVALID")]))
        missing_elements = state.get_missing_elements()
        assert len(missing_elements) == 1





