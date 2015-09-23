from app import state_builder
from app.attribute_builder import AttributeBuilder
from models.element_state import ElementState


class ElementComparer(object):
    def __init__(self, driver):
        self.driver = driver

    def compare_elements(self, element1, element2):
        assert isinstance(element1, ElementState)
        assert isinstance(element2, ElementState)

        points = 0
        total = 0

        builder1 = AttributeBuilder(element1)
        element1_attributes = builder1.total_attributes

        builder2 = AttributeBuilder(element2)
        element2_attributes = builder2.total_attributes

        for attribute in element1_attributes:
            total+=1
            if attribute not in element2_attributes:
                points+=1

        attribute_percentage = points / total

        x_diff = abs((element1.location.x- element2.location.x))
        y_diff = abs(element1.location.y - element2.location.y)
        w_diff = abs(element1.location.width- element2.location.width)
        h_diff = abs(element1.location.height - element2.location.height)

        total = x_diff + y_diff + w_diff + h_diff

        total_perc = total / 4

        total = (total_perc + attribute_percentage) / 2

        return total





