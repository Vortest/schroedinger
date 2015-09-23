from app.locator_builder import LocatorBuilder
from app.webelement import WebElement
from models.element_state import ElementState


def build_element(driver, element):
    builder = LocatorBuilder(driver, element)
    locators = builder.get_locators()
    if(len(locators)) > 0:
        new_element = ElementState(locators=locators, html=element.html, screenshot=element.screenshot_as_base64)
        new_element.set_location(element)
        new_element.save()
        WebElement(driver,new_element.locators).highlight()
        return new_element
