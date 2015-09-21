import logging
from selenium.common.exceptions import StaleElementReferenceException
from models.element import Element
from webelement import WebElement
from locator_builder import LocatorBuilder
from page_parser import PageParser
from models.state import State
import time
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
    elements = parser.get_all_elements()
    elements = sorted(elements,key=lambda element: element.area,reverse=True)
    print "Found %s elements " % len(elements)
    for element in elements:
        builder = LocatorBuilder(driver, element)
        locators = builder.get_locators()
        if(len(locators)) > 0:
            new_element = Element(locators=locators, html=element.html[:255], screenshot=element.screenshot_as_base64)
            new_element.set_location(element)
            new_element.save()
            locator_elements.append(new_element)
            WebElement(driver,new_element.locators).highlight()
    screenshot = driver.get_screenshot_as_base64()
    state = State(elements=locator_elements,url=driver.current_url, html=driver.html, screenshot = screenshot)
    return state

def get_blank_state():
    return State.objects(url="").first()

def get_extra_elements(driver, state):
    actual_state = get_state(driver)
    diff_state = actual_state - state
    return diff_state.elements


