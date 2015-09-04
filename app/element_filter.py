from webelement_wrapper import WebElement
def filter_visible_elements(elements):
    visible_elements = []
    for ele in elements:
        if ele.is_displayed and ele.size["height"] > 0 and ele.size["width"] > 0 and ele.location["x"] > 0 and ele.location["y"] > 0:
            visible_elements.append(ele)
    return visible_elements

def filter_by(elements, attribute, value):
    filtered_elements = []
    for element in elements:
       if getattr(element,attribute) == value:
           filtered_elements.append(element)
    return filtered_elements

def filter_no_children(elements):
    final_elements = []
    for ele in elements:
        if "<" not in ele.inner_html:
            final_elements.append(ele)
    return final_elements

def login_fields(elements):
    for element in elements:

        if element.tag_name in login_fields:
            return element

def filter_inputs(elements):
    new_elements = []
    for element in elements:
        if element.tag_name == "input":
            new_elements.append(element)
    return new_elements

def filter_elements(elements, tag, attribute):
    new_elements = []
    for element in elements:
        if element.is_displayed() and element.tag_name == tag and element.get_attribute(attribute[0]) == attribute[1]:
            new_elements.append(element)
    return new_elements