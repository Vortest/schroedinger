from selenium.webdriver.common.by import By
from app.element_matcher import ElementMatcher, ElementType

from app.webelement import WebElement
from app.test_base import TestBase
from models.element_state import Locator, ElementType


class TestElementMatcher(TestBase):
    def test_email(self):
        matcher = ElementMatcher()
        self.driver.get("https://accounts.google.com/ServiceLogin")
        element = self.driver.find_element(By.ID,"Email")
        type = matcher.match(element)
        assert type == ElementType.USERNAME, type

    def test_password(self):
        matcher = ElementMatcher()
        self.driver.get("https://accounts.google.com/ServiceLogin")
        element = self.driver.find_element(By.ID,"Passwd")
        type = matcher.match(element)
        assert type == ElementType.PASSWORD, type

    def test_login_button(self):
        matcher = ElementMatcher()
        self.driver.get("https://www.grubhub.com")
        element = self.driver.find_element(By.CSS_SELECTOR,".topNav-signIn")
        type = matcher.match(element)
        assert type == ElementType.LOGIN, type

    def test_search_button(self):
        matcher = ElementMatcher()
        self.driver.get("https://www.grubhub.com")
        element = self.driver.find_element(By.ID,"ghs-startOrder-searchBtn")
        type = matcher.match(element)
        assert type == ElementType.SEARCH, type


