import logging


class State(object):
    def __init__(self, elements, url):
        self.elements = elements
        self.url = url

    def __eq__(self, other):
        for element in self.elements:
            if element not in other.elements:
                logging.debug("Element not in other.elements")
                return False
        logging.debug("State must be the same!")
        return True

    def __repr__(self):
        return "State(url=%s) %s Elements" % (self.url, len(self.elements))