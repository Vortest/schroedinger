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
