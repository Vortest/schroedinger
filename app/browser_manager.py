import browser_launcher
import logging

class BrowserManager(object):
    _drivers = {}

    @staticmethod
    def get_driver(name):
        if name not in BrowserManager._drivers:
            BrowserManager._drivers[name] = browser_launcher.launch_browser()
        return BrowserManager._drivers[name]





