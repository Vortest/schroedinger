import abc
import logging
import threading,Queue,time,sys,traceback
from app.webelement import WebElement
from app.worker import Worker
from threading import Thread, current_thread, currentThread
from app import state_builder,action_builder, browser_launcher, state_crawler
from app import url_parser

class UrlCrawlerWorker(Worker):
    def process_item(self, url):
        print "Processing %s %s" % (currentThread(),url)
        self.driver = browser_launcher.launch_browser()
        state =  self.crawl_url(url)
        print "Found %s elements" % state.elements
        self.driver.quit()
        print "UrlCrawler finished processing %s" % url
        return state

    def crawl_url(self, url):
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
        return initial_state

class StateCrawlerWorker(Worker):
    def process_item(self, state):
        print "Processing %s %s" % (currentThread(),state)
        self.driver = browser_launcher.launch_browser()
        state =  self.crawl_state(state)
        print "Found %s elements" % state.elements
        self.driver.quit()
        for action in state.actions:
            print "adding state to Q %s" % action.end_state
            self.put(action.end_state)
        print "StateCrawler finished processing %s" % state
        return state


    def crawl_state(self, state):
        for element in state.elements:
            try:
                state.initialize_state(self.driver)
                print "Loaded initial state %s" % state.id
                webelement = WebElement(self.driver, element.locators)
                if webelement.is_displayed():
                    print "Clicking %s" % element
                    webelement.click()
                    domain = url_parser.get_domain_from_url(self.driver.current_url)
                    if domain not in state.url:
                        print "State is different domain"
                        break
                    if state.is_state_present(self.driver):
                        print "looks like this is the same state"
                    else:
                        new_state = state_builder.get_current_state(self.driver)
                        new_state.save()
                        print 'new state found at %s %s' % (self.driver.current_url,new_state.id)
                        click_action = action_builder.get_click_action(element, state, new_state)
                        new_state.init_actions = state.init_actions
                        new_state.init_actions.append(click_action)
                        new_state.save()
                        state.actions.append(click_action)
                        state.save()
                        self.put(new_state)
                else:
                    logging.error("Could not reproduce state %s element %s not present" % (state, element))
            except Exception as e:
                print "Couldn't crawl element %s %s" % (element.locators, str(e))
        return state


