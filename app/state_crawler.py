import logging
from app import action_builder
from app.webelement import WebElement
from app import state_builder

class StateCrawler(object):
    def __init__(self, driver):
        self.driver = driver

    def crawl_state(self, state):
        for element in state.elements:
            try:
                state.initialize_state(self.driver)
                print "Loaded initial state %s" % state.id
                webelement = WebElement(self.driver, element.locators)
                if webelement.is_displayed():
                    webelement.click()
                    new_state = state_builder.get_current_state(self.driver)
                    if new_state == state:
                        print "looks like this is the same state"
                    else:
                        new_state.save()
                        print 'new state found at %s %s' % (self.driver.current_url,new_state.id)
                        click_action = action_builder.get_click_action(element, state, new_state)
                        new_state.init_actions = state.init_actions
                        new_state.init_actions.append(click_action)
                        new_state.save()
                        state.actions.append(click_action)
                        state.save()
                else:
                    logging.error("Could not reproduce state %s element %s not present" % (state, element))
            except Exception as e:
                print "Couldn't crawl element %s %s" % (element.locators, str(e))

    def crawl_url(self, url, deep=False):
        self.driver.get(url)
        initial_state = state_builder.get_current_state(self.driver)
        initial_state.save()
        blank_state = state_builder.get_blank_state()
        blank_state.save()
        nav_action = action_builder.get_nav_action(url,initial_state)
        nav_action.save()
        initial_state.init_actions = [nav_action]
        initial_state.save()
        print "Saved initial state %s" % initial_state.id
        if deep:
            self.crawl_state(initial_state)
        return initial_state.id


