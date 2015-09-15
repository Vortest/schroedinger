import datetime
import logging

from flask import url_for
from api import db
from app.locator_builder import LocatorBuilder
from app.page_parser import PageParser
from app.webelement import WebElement
from models.action import Action
from models.element import Element


class State(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    html = db.StringField(required=False)
    screenshot = db.StringField(required=False)
    elements = db.ListField(db.ReferenceField(Element))
    actions = db.ListField(db.ReferenceField(Action))
    init_actions = db.ListField(db.ReferenceField(Action), required=False)
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
        logging.debug("Verifying state %s %s" % (self.id, self.url))
        for element in self.elements:
            try:
                WebElement(driver,element.locators).highlight()
            except Exception as e:
                logging.error(str(e))


    def get_missing_elements(self,driver):
        missing_elements = []
        for element in self.elements:
            if not WebElement(driver,element.locators).is_present():
                missing_elements.append(element)
        return missing_elements

    def get_replaced_elements(self,driver, new_state):
        replaced_elements = []
        for element in new_state.elements:
            if element not in self.elements:
                replaced_elements.apppend(element)
        return replaced_elements

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

    def initialize_state(self, driver):
        for action in self.init_actions:
            action.execute(driver)
        self.verify_state(driver)



    def get_current_state(self, driver):
        try:
            return self.get_state(driver)
        except Exception as e:
            logging.exception(str(e))
            return self.get_state(driver)

    def get_state(self, driver):
        parser = PageParser(driver)
        locator_elements = []
        elements = parser.get_all_elements()
        print "Found %s elements " % len(elements)
        for element in elements:
            builder = LocatorBuilder(driver, element)
            locators = builder.get_locators()
            if(len(locators)) > 0:
                new_element = Element(locators=locators, html=element.html[:255], screenshot=element.screenshot_as_base64)
                new_element.set_location(element)
                new_element.save()
                locator_elements.append(new_element)
                WebElement(driver,new_element.locators).highlight()
        screenshot = driver.get_screenshot_as_base64()
        state = State(elements=locator_elements,url=driver.current_url, html=driver.html, screenshot = screenshot)
        return state

    def get_blank_state(self):
        return State.objects(url="").first()