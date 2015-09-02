from testfixtures import Comparison as C

class StateComparer(object):
    def __init__(self,element1, element2):
        self.element1 = element1
        self.element2 = element2

    def compare_elements(self):
