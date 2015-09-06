import base64
import os
from PIL import Image
import StringIO
import logging

def get_element_image(driver, element):
    screenshot = driver.get_screenshot_as_base64()
    full_image= get_image_from_base64(screenshot)
    location = element.location
    size = element.size
    width = size['width']
    height = size['height']
    left = location['x']
    top = location['y']
    right = location['x'] + width
    bottom = location['y'] + height

    new_image = full_image.crop((left,top,right,bottom))

    return new_image

def get_image_from_base64(value):
    return Image.open(StringIO.StringIO(base64.decodestring(value)))

def get_base64_from_image(image):
    string = get_image_string(image)
    value = base64.b64encode(string)
    return value

def get_image_string(image):
        output = StringIO.StringIO()
        image.save(output,format="png")
        text_value= output.getvalue()
        output.close()
        return text_value