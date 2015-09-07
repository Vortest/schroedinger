from app.test_base import TestBase
import app.images as images

class TestImages(TestBase):
    def test_get_element_image(self):
        self.driver.get("http://stackoverflow.com/")
        element = self.driver.find_element_by_id('hlogo')
        image = images.get_element_image(self.driver, element)
        assert image.size != (0,0) and image.size is not None
        text = images.get_image_string(image)
        print text

    def test_get_image_string(self):
        self.driver.get("http://stackoverflow.com/")
        element = self.driver.find_element_by_id('hlogo')
        image = images.get_element_image(self.driver, element)
        text = images.get_image_string(image)

    def test_get_image_from_base64(self):
        self.driver.get("http://www.google.com/")
        screenshot = self.driver.get_screenshot_as_base64()
        image = images.get_image_from_base64(screenshot)
        assert image.size != (0,0) and image.size is not None

    def test_get_base64_from_image(self):
        self.driver.get("http://stackoverflow.com/")
        element = self.driver.find_element_by_id('hlogo')
        image = images.get_element_image(self.driver, element)
        value = images.get_base64_from_image(image)
        new_image = images.get_image_from_base64(value)

        assert new_image.size == image.size



