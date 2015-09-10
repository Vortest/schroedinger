import unittest
from selenium.webdriver.common.by import By
from app.test_base import TestBase
from models.action import Action
from models.command import Command
from models.element import Element, Locator
from models.page import Page
from models.post import Post, Comment
from app.browser_manager import BrowserManager
from models.state import State


class TestPage(unittest.TestCase):

    def test_page(self):
        default_state = State.objects().first()
        states = State.objects[:5]
        page = Page(url="http://www.google.com/", default_state=default_state, states=states)
        page.save()
        assert len(page.states) > 0




