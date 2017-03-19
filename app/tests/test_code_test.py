import logging
import unittest
import exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from app.browser_manager import BrowserManager
from app.browser_session import BrowserSession
from app.test_base import TestBase
from app.webdriver_element import WebdriverElement
from app.webelement import WebElement
from models.suite_config import SuiteConfig, RunConfig
import app.by
from app.webdriver_adapter import WebdriverAdapter

class GrubhubHomePage(object):
    sign_in_button = WebdriverElement("grubhubhome","Sign In")

    def sign_in(self):
        self.sign_in_button.click()
        return GrubhubLoginPage()

class GrubhubLoginPage(object):
    username = WebdriverElement("grubhublogin","Email")
    password = WebdriverElement("grubhublogin","Password")
    signin = WebdriverElement("grubhublogin","Sign In")

    def login(self, username, password):
        self.username.send_keys(username)
        self.password.send_keys(password)
        self.loginbutton.click()


class FacebookLoginPage(object):
    username = WebdriverElement("loginpage","Email")
    password = WebdriverElement("loginpage","Password")
    loginbutton = WebdriverElement("loginpage","Log In")

    def login(self, username, password):
        self.username.send_keys(username)
        self.password.send_keys(password)
        self.loginbutton.click()

class TestCodeTest(TestBase):
    def test_fb(self):
        self._driver = BrowserManager.get_driver("")
        self.driver.get("https://www.facebook.com")
        loginpage = FacebookLoginPage()
        loginpage.login("kitchener.brian@gmail.com","Qubit123!")

    def test_grubhub(self):
        self._driver = BrowserManager.get_driver("")
        self.driver.get("https://www.grubhub.com")
        home = GrubhubHomePage()
        home.sign_in().login("kitchener.brian@gmail.com","Qubit123!")


