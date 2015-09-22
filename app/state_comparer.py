from app import state_builder
from app.element_comparer import ElementComparer
class StateComparer(object):
    def __init__(self, driver):
        self.driver = driver

    def compare_states(self, state1, state2):
        missing_state = state1 - state2
        extra_state = state2 - state1
        return (missing_state,extra_state)

    def compare_to_live_state(self, state):
        new_state = state_builder.get_current_state(self.driver)
        state = self.compare_states(state, new_state)
        return (len(state[0].elements),len(state[1].elements))

    def match_elements(self, state1, state2):
        assert len(state1.elements) == len(state2.elements)
        diff_state = self.compare_states(state1, state2)
        missing_elements = diff_state[0].elements
        extra_elements = diff_state[1].elements
        fixed_elements = []
        for missing_element in missing_elements:
            highest = -1
            best_fit = None
            for extra_element in extra_elements:
                value = ElementComparer(self.driver).compare_elements(missing_element, extra_element)
                if value > highest:
                    highest = value
                    best_fit = (missing_element,extra_element)
            fixed_elements.append(best_fit)
        return fixed_elements

