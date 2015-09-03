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

    def __sub__(self, other):
        new_elements = []
        for element in other.elements:
            if element not in self.elements:
                new_elements.append(element)
        return State(new_elements, self.url)

    def __repr__(self):
        return "State(url=%s) %s Elements %s" % (self.url, len(self.elements),self.elements)