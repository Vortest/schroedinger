import datetime

from flask import url_for
from api import db
from app.webelement import WebElement
from models.action import Action
from models.element import Element


class State(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    html = db.StringField(max_length=255, required=False)
    screenshot = db.StringField(required=False)
    elements = db.ListField(db.ReferenceField(Element))
    actions = db.ListField(db.ReferenceField(Action))
    url = db.StringField(max_length=255, required=True)

    meta = {
        'allow_inheritance': True,
        'indexes': ['-created_at'],
        'ordering': ['-created_at']
    }

    def __eq__(self, other):
        if other is None:
            return False
        for element in self.elements:
            if element not in other.elements:
                return False
        return True

    def __sub__(self, other):
        """
        Returns a State representing the difference in elements
        :param other:
        :return:
        """
        new_elements = []
        for element in self.elements:
            if element not in other.elements:
                new_elements.append(element)
        return State(elements=new_elements, url=self.url)

    def __add__(self, other):
        """
        Combines two states together
        :param other:
        :return:
        """
        all_elements = self.elements.extend(other.elements)
        return State(elements=all_elements,url=self.url)

    def __div__(self, other):
        """
        Returns the elements not shared with the second state
        :param other:
        :return:
        """
        new_elements = []
        for element in self.elements:
            if element in other.elements:
                new_elements.append(element)
        return State(elements=new_elements,url=self.url)

    def __repr__(self):
        return "State(url=%s) %s Elements %s" % (self.url, len(self.elements),self.elements)

    def get_web_elements(self, driver):
        webelements = []
        for element in self.elements:
            webelements.append(WebElement(driver, element.locators))
        return webelements

    def verify_state(self,driver):

        for element in self.elements:
            WebElement(driver,element.locators).highlight()

    def get_missing_elements(self,driver):
        missing_elements = []
        for element in self.elements:
            if not WebElement(driver,element.locators).is_present():
                missing_elements.append(element)
        return missing_elements

    def update_element(self, old_element, new_element):
        self.elements.remove(old_element)
        self.elements.append(new_element)

    def remove_element(self, element):
        self.elements.remove(element)

    def add_element(self, element):
        self.elements.append(element)

    def get_html_info(self):
        self.element_html = []
        for element in self.elements:
            self.element_html.append(element.html)