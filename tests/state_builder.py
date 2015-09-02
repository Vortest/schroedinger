from page_parser import PageParser


class StateBuilder(object):
    def __init_(self,driver):
        self.driver = driver
        self.parser = PageParser()

    def get_current_state(self):
        PagePar