from app import action_builder
from app.state_builder import StateBuilder

class Crawler(object):
    def __init__(self, driver):
        self.driver = driver

    def crawl_current(self, init_actions):
        state_builder = StateBuilder(self.driver)
        initial_state = state_builder.get_current_state()
        initial_state.save()
        initial_state.init_actions = init_actions
        initial_state.save()
        print "Saved initial state %s" % initial_state.id
        for element in initial_state.get_web_elements(self.driver):
            try:
                for action in init_actions:
                    action.execute(self.driver)
                if(element.is_displayed()):
                    element.click()
                    new_state = state_builder.get_current_state()
                    if new_state == initial_state:
                        print "looks like this is the same state"
                    else:
                        new_state.save()
                        click_action = action_builder.get_click_action(element, initial_state, new_state)
                        initial_state.actions.append(click_action)
                        initial_state.save()
                        new_state.init_actions = init_actions
                        new_state.init_actions.append(click_action)
                        new_state.save()
                        print 'new state found at %s %s' % (self.driver.current_url,new_state.id)
                else:
                    print "Could not reproduce state %s" % initial_state.id
            except Exception as e:
                print "Couldn't crawl element %s %s" % (element.locators, str(e))

    def crawl_url(self, url, deep=False):
        self.driver.get(url)
        state_builder = StateBuilder(self.driver)
        initial_state = state_builder.get_current_state()
        initial_state.save()
        blank_state = state_builder.get_blank_state()
        blank_state.save()
        nav_action = action_builder.get_nav_action(url,start_state=blank_state,end_state=initial_state)
        nav_action.save()
        initial_state.init_actions = [nav_action]
        initial_state.save()
        print "Saved initial state %s" % initial_state.id
        new_states = []
        for element in initial_state.get_web_elements(self.driver):
            try:
                self.driver.get(url)
                if(element.is_displayed()):
                    element.click()
                    new_state = state_builder.get_current_state()
                    if new_state == initial_state:
                        print "looks like this is the same state"
                    else:
                        new_state.save()
                        click_action = action_builder.get_click_action(element, initial_state, new_state)
                        initial_state.actions.append(click_action)
                        initial_state.save()
                        new_state.init_actions = [nav_action, click_action]
                        new_state.save()
                        print 'new state found at %s %s' % (self.driver.current_url,new_state.id)
            except Exception as e:
                print "Couldn't crawl element %s %s" % (element.locators, str(e))
        print "%s states" % len(new_states)
        for state in new_states:
            print state



