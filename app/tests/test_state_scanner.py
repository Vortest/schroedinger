from app import state_builder
from app.test_base import TestBase
from app.state_scanner import StateScanner

class TestStateScanner(TestBase):
    def test_scanner(self):
        self.driver.get("http://www.google.com")

        state = state_builder.get_current_state(self.driver)
        scanner = StateScanner(self.driver)

        missing_elements = scanner.check_state(state)
        assert len(missing_elements) == 0