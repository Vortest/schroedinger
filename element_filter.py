from webelement_wrapper import WebElement
def filter_visible_elements(elements):
    for ele in elements:
        if ele.is_displayed and ele.size["height"] > 0 and ele.size["width"] > 0 and ele.location["x"] > 0 and ele.location["y"] > 0: yield ele

def filter_by(elements, attribute, value):
    for element in elements:
       if getattr(element,attribute) == value: yield element


def login_fields(elements):
    for element in elements:
        if element.tag_name in login_fields:
            pass