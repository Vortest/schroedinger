from models.element_state import ElementState
from models.page import Page
from models.state import State
from app import state_builder, page_parser
class WebdriverAdapter(object):
    def __init__(self, driver, page, key):
        self.driver = driver
        self.page = page
        self.key = key

    def get_locators(self):
        state = self.get_state()
        for element in state.elements:
            if hasattr(element, "name") and self.key == element.name:
                return element.locators
        print "couldn't find element in state by name, looking in html"
        for element in state.elements:
            if self.key in element.html:
                print "Found element that matches the key %s" % element.html
                element.name = self.key
                element.save()
                return element.locators
        for element in state.elements:
            print "Couldn't map %s an element to %s" % (self.key, element)
        return None

    def get_state(self):
        url = self.driver.current_url
        page = Page.objects(url=url).first()
        if page is None:
            self.driver.get(url)
            default_state = state_builder.get_current_state(self.driver)
            default_state.name = self.page
            default_state.save()
            page  = Page(url=url, default_state=default_state, states=[default_state])
            page.name = self.page
            page.save()
        for state in page.states:
            if state.name == self.page:
                print "Found state %s" % state.name
                return state
        print "State not found, creating new state"
        new_state = state_builder.get_current_state(self.driver)
        new_state.save()
        new_state.name = self.page
        page.states.append(new_state)
        page.save()
        return new_state
