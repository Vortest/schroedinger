import base64
from io import BytesIO
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
    left = int(location['x'])
    top = int(location['y'])
    right = left + width
    bottom = top + height

    new_image = full_image.crop((left,top,right,bottom))
    return new_image

def get_image_from_base64(value):
    return Image.open(StringIO.StringIO(base64.decodestring(value)))

def get_base64_from_image(image):
    output = StringIO.StringIO()
    image.save(output,format="png")
    string = output.getvalue()
    output.close()
    base64_string = base64.b64encode(string)
    return base64_string


def get_png_from_image(image):
    output = BytesIO()
    image.save(output,format="png")
    png = output.getvalue()
    output.close()
    return png