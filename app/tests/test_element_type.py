from selenium.webdriver.common.by import By
from app.element_type import ElementType
from app.test_base import TestBase
from app.webelement import WebElement
from models.element_state import Locator


class ElementTypeTest(TestBase):
    def test_input_is_editable(self):
        self.driver.get("http://www.google.com")
        locators = [Locator(by=By.NAME,value="q")]
        element = WebElement(self.driver, locators)
        typer = ElementType(element)
        assert typer.is_editable()

    def test_button_not_editable(self):
        self.driver.get("http://www.google.com")
        locators = [Locator(by=By.LINK_TEXT,value="Images")]
        element = WebElement(self.driver, locators)
        typer = ElementType(element)
        assert not typer.is_editable()

    def test_button_is_clickable(self):
        self.driver.get("http://www.google.com")
        locators = [Locator(by=By.LINK_TEXT,value="Images")]
        element = WebElement(self.driver, locators)
        typer = ElementType(element)
        assert typer.is_clickable()

    def test_button_is_clickable(self):
        self.driver.get("http://www.google.com")
        locators = [Locator(by=By.LINK_TEXT,value="Images")]
        element = WebElement(self.driver, locators)
        typer = ElementType(element)
        assert typer.is_clickable()