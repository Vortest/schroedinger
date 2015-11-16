from app.page_parser import PageParser
from app.test_base import TestBase
from app import state_builder

class GenerateFormsTest(TestBase):
    def test_generate_login_test(self):
        self.driver.get("http://www.facebook.com")
        state = state_builder.get_current_state(self.driver)

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