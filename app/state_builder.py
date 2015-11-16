import logging
from selenium.common.exceptions import StaleElementReferenceException
from models.element_state import ElementState
from webelement import WebElement
from locator_builder import LocatorBuilder
from page_parser import PageParser
from models.state import State
import time
from app import element_builder

def get_url_state(driver, url):
    driver.get(url)
    return get_current_state(driver)

def get_current_state(driver):
    try:
        time.sleep(3)
        return get_state(driver)
    except Exception as e:
        logging.exception(str(e))
        return get_state(driver)

def get_state(driver):
    parser = PageParser(driver)
    locator_elements = []
    elements = parser.get_usual_elements()
    print "Found %s elements " % len(elements)
    for element in elements:
        new_element = element_builder.build_element(driver, element)
        if new_element is not None:
            locator_elements.append(new_element)

    screenshot = driver.get_screenshot_as_base64()
    state = State(elements=locator_elements,url=driver.current_url, html=driver.html, screenshot = screenshot)
    return state

def get_blank_state():
    return State.objects(url="").first()

def get_extra_elements(driver, state):
    actual_state = get_state(driver)
    diff_state = actual_state - state
    return diff_state.elements

def get_new_state(driver, old_state):
    parser = PageParser(driver)
    state_elements = []
    live_elements = parser.get_all_elements()
    #first look for the old elements that are still present
    for element in old_state.elements:
        webelement = WebElement(driver, element.locators)
        if webelement.is_present(1):
            webelement.highlight(color="green")
            if webelement in live_elements:
                state_elements.append(element)
                live_elements.remove(webelement)

    #look for any changed elements
    for element in live_elements:
        element.highlight(color="blue")
        new_element_state = element_builder.build_element(driver, element)
        state_elements.append(new_element_state)

    return State(elements = state_elements, url=driver.current_url, html=driver.html, screenshot = driver.get_screenshot_as_base64())