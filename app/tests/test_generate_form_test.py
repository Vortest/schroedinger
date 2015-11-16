from selenium.webdriver.common.by import By
from app.element_matcher import ElementMatcher
from models.element_state import ElementType
from app.page_parser import PageParser
from app.test_base import TestBase
from app import state_builder

class GenerateFormsTest(TestBase):
    def test_generate_form_test(self):
        self.driver.get("http://www.facebook.com")
        forms = self.driver.find_elements(By.TAG_NAME,"form")
        matcher = ElementMatcher()
        for form in forms:
            print "Form %s" % form.html
            inputs = form.find_elements(By.TAG_NAME,"input")
            for input in inputs:
                input.highlight(color="green")
                type = matcher.match(input)
                #print "%s %s" % (type, input.html)


        #get the page or state
        #find all the fields
        #if there is a login link
        #if there is a username or email field
        #if there is a password field
        #if there is a submit button
        #if there is a search field

        #zip
        #email
        #address
        #name
        #first name

        #open page
        #check conditions
        #if conditions match do them
            #what are conditions? They are things we can tell aboutthe page.  Things such as an input field. a search
            #field.
        #after each condition, check if the state changed.

        #type into all fields, click submit.  check new state.