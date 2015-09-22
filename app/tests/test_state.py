from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from app.webelement import WebElement
from app import state_builder
from app.test_base import TestBase
from models.action import Action
from models.command import Command
from models.element import Locator, Element


class StateTest(TestBase):
    def test_state_builder(self):
        self.url = "http://www.google.com/"
        self.driver.get(self.url)
        state = state_builder.get_current_state(self.driver)
        for i in range(0,5):
            self.driver.get(self.url)
            state.verify_state(self.driver)

    def test_compare_same_page(self):
        self.url = "http://www.google.com/"
        self.driver.get(self.url)
        state = state_builder.get_current_state(self.driver)

        self.url2 = "http://www.google.com/"
        self.driver.get(self.url2)
        state2 = state_builder.get_current_state(self.driver)
        assert state == state2

    def test_compare_same_page_fails_missing_element(self):
        self.url = "http://www.google.com/"
        self.driver.get(self.url)
        state = state_builder.get_current_state(self.driver)
        state.elements.remove(state.elements[0])
        self.url2 = "http://www.google.com/"
        self.driver.get(self.url2)
        state2 = state_builder.get_current_state(self.driver)
        state2.elements.remove(state.elements[6])
        assert state != state2

    def test_compare_diff_page(self):
        self.url = "http://www.google.com/"
        self.driver.get(self.url)
        state = state_builder.get_current_state(self.driver)

        self.url2 = "http://www.bluemodus.com/"
        self.driver.get(self.url2)
        state2 = state_builder.get_current_state(self.driver)
        assert state != state2

    def test_compare_similar_pages(self):
        self.url = "http://www.google.com/"
        self.driver.get(self.url)
        state = state_builder.get_current_state(self.driver)

        self.url2 = "http://www.google.co.uk/"
        self.driver.get(self.url2)
        state2 = state_builder.get_current_state(self.driver)

        assert state != state2


    def test_subtract_state(self):
        self.url = "http://www.google.com/"
        self.driver.get(self.url)
        state = state_builder.get_current_state(self.driver)

        self.url2 = "http://www.google.co.uk/"
        self.driver.get(self.url2)
        state2 = state_builder.get_current_state(self.driver)

        uk_diff = state2 - state
        uk_diff.verify_state(self.driver
                             )

    def test_divide_state(self):
        self.url = "http://www.google.com"
        self.driver.get(self.url)
        state = state_builder.get_current_state(self.driver)

        self.url2 = "http://www.google.co.uk"
        self.driver.get(self.url2)
        state2 = state_builder.get_current_state(self.driver)

        shared_state = state2 / state
        shared_state.verify_state(self.driver)

        self.driver.get("http://www.google.com/")
        shared_state.verify_state(self.driver)

    def test_verify_state(self):
        self.url = "http://www.google.com"
        self.driver.get(self.url)
        state = state_builder.get_current_state(self.driver)
        self.driver.get(self.url)
        state.verify_state(self.driver)

    def test_get_missing_elements(self):
        self.url = "http://www.google.com"
        self.driver.get(self.url)
        state = state_builder.get_current_state(self.driver)
        state.elements.append(WebElement(self.driver, [Locator(by=By.CSS_SELECTOR, value="INVALID")]))
        missing_elements = state.get_missing_elements(self.driver)
        assert len(missing_elements) == 1

    def test_remove_missing_elements(self):
        self.url = "http://www.google.com"
        self.driver.get(self.url)
        state = state_builder.get_current_state(self.driver)
        state.elements.append(WebElement(self.driver, [Locator(by=By.CSS_SELECTOR, value="INVALID")]))
        missing_elements = state.get_missing_elements(self.driver)
        for element in missing_elements:
            print "removing %s" % element
            state.remove_element(element)
            assert element not in state.elements

    def test_add_new_element(self):
        self.url = "http://www.google.com"
        self.driver.get(self.url)
        state = state_builder.get_current_state(self.driver)
        num_elements = len(state.elements)
        state.remove_element(state.elements[1])
        new_state = state_builder.get_current_state(self.driver)
        diff_state = new_state - state
        assert len(diff_state.elements) == 1
        for element in diff_state.elements:
            state.add_element(element)

        state.verify_state(self.driver)

        assert len(state.elements) == num_elements

    def test_init_state(self):
        self.url = "http://www.google.com"
        blank_state = state_builder.get_blank_state()
        blank_state.save()
        self.driver.get(self.url)
        state = state_builder.get_current_state(self.driver)
        state.save()
        element = Element(locators = [Locator(by=By.NAME,value="q")])
        element2= Element(locators= [Locator(by=By.NAME,value="btnG")])
        element.save()
        element2.save()
        nav_command = [Command(command=Command.NAVIGATE,params="http://www.google.com/")]
        type_command = [Command(command=Command.SENDKEYS,element = element,params="Something"),
                        Command(command=Command.SENDKEYS,element = element,params=Keys.ENTER)]


        action = Action(name = "Navigate",steps=nav_command,start_state=blank_state, end_state=state)
        action.save()
        action2 = Action(name = "Search",steps=type_command,start_state=state, end_state=blank_state)
        action2.save()

        action.execute(self.driver)
        action2.execute(self.driver)
        time.sleep(5)
        new_state = state_builder.get_current_state(self.driver)
        new_state.save()
        action2.end_state = new_state
        action2.save()

        new_state.init_actions = [action,action2]
        new_state.save()
        state_id = new_state.id

        print state_id

        self.driver.get("http://www.msn.com/")

        new_state.initialize_state(self.driver)




