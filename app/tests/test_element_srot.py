from app import state_builder
from app.test_base import TestBase


class TestElementSort(TestBase):
    def test_sort_elements(self):
        self.url = "http://www.percolate.com/platform"
        self.driver.get(self.url)
        state = state_builder.get_current_state(self.driver)
