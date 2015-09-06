from app.state_builder import StateBuilder
from app.test_base import TestBase


class TestElementSort(TestBase):
    def test_sort_elements(self):
        self.url = "http://www.percolate.com/platform"
        self.driver.get(self.url)
        builder = StateBuilder(self.driver)
        state = builder.get_current_state()
