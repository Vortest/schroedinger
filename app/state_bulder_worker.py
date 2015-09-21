import abc
import threading,Queue,time,sys,traceback
from app import browser_manager
from app import state_builder
from app.worker import Worker
from threading import Thread, current_thread, currentThread
from app import browser_launcher

class StateBuilderWorker(Worker):

    def process_item(self, value):
        print "Processing %s %s" % (currentThread(),value)
        driver = browser_launcher.launch_browser()
        state =  state_builder.get_url_state(driver, value)
        print "Found %s elements" % state.elements
        driver.quit()
        return state
