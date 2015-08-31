from browser_manager import BrowserManager
from webelement_wrapper import WebElement
from selenium.common import exceptions

class Element(WebElement):

    def __init__(self, locators):
        assert isinstance(locators,list)
        assert isinstance(locators[0],tuple)
        self._element = None
        self.locators = locators

    @property
    def driver(self):
       return BrowserManager.get_driver()

    @property
    def element(self):
       if self._element is None or self._element.is_stale():
           for locator in self.locators:
               eles = self.driver.find_elements(locator[0],locator[1])
               if len(eles) > 0:
                   self._element = eles[0]
                   self.by = locator[0]
                   self.value = locator[1]
                   return self._element
           raise exceptions.NoSuchElementException("Could not find an element matching any of the following locators: {}".format(self.locators))
       else:
           return self._element
