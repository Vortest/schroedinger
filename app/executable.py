import abc

class Executable(object):
    def get_steps(self):
        return self.steps

    def execute(self, driver):
        self.driver = driver
        for step in self.steps:
                step.execute(driver)


