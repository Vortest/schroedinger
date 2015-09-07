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

    def test_find_similar(self):
        self.url = "http://www.percolate.com/platform"
        self.driver.get(self.url)
        builder = StateBuilder(self.driver)
        state = builder.get_current_state()

        self.url2 = "http://www.percolate.com/services"
        self.driver.get(self.url2)
        builder = StateBuilder(self.driver)
        state2 = builder.get_current_state()

        for element in state2.elements:
            if element in state.elements:
                print "Found %s %s" % (element.locators, element.html)
                element.highlight



