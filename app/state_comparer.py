from app import state_builder

class StateComparer(object):
    def __init__(self, driver):
        self.driver = driver

    def compare_state(self, state1, state2):
        missing_state = state1 - state2
        extra_state = state2 - state1
        return (missing_state,extra_state)

    def get_compare(self, state):
        new_state = state_builder.get_current_state(self.driver)
        state = self.compare_state(state, new_state)
        return (len(state[0].elements),len(state[1].elements))