import logging


class State(object):
    def __init__(self, elements, url):
        self.elements = elements
        self.url = url

    def __eq__(self, other):
        for element in self.elements:
            if element not in other.elements:
                return False
        return True

    def __sub__(self, other):
        """
        Returns a State representing the difference in elements
        :param other:
        :return:
        """
        new_elements = []
        for element in self.elements:
            if element not in other.elements:
                new_elements.append(element)
        return State(new_elements, self.url)

    def __add__(self, other):
        """
        Combines two states together
        :param other:
        :return:
        """
        all_elements = self.elements.extend(other.elements)
        return State(all_elements,self.url)

    def __div__(self, other):
        """
        Returns the elements not shared with the second state
        :param other:
        :return:
        """
        new_elements = []
        for element in self.elements:
            if element in other.elements:
                new_elements.append(element)
        return State(new_elements,self.url)

    def __repr__(self):
        return "State(url=%s) %s Elements %s" % (self.url, len(self.elements),self.elements)

    def verify_state(self):
        for element in self.elements:
            element.highlight()

    def get_missing_elements(self):
        missing_elements = []
        for element in self.elements:
            if not element.is_present():
                missing_elements.append(element)
        return missing_elements

    def update_element(self, old_element, new_element):
        self.elements.remove(old_element)
        self.elements.append(new_element)

    def remove_element(self, element):
        self.elements.remove(element)

    def add_element(self, element):
        self.elements.append(element)

