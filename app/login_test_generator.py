from app import state_builder,action_builder
from app.webelement import WebElement
from models.action import Action
from models.command import Command
from models.element_state import ElementType
from models.test import Test

class LoginTestGenerator(object):
    def __init__(self, driver, url, config):
        self.driver = driver
        self.url = url
        self.config = config
        
    def web_element(self, element):
        field = WebElement(self.driver, element.locators)
        return field

    def generate(self):
        actions = []
        self.driver.get(self.url)
        start_state = state_builder.get_current_state(self.driver)
        start_state.save()
        action = action_builder.get_nav_action(self.url, start_state)
        action.save()
        actions.append(action)
        self.click_login = self.get_click_login_action(start_state)
        if self.click_login is not None:
            new_state = self.click_login.end_state
        else:
            new_state = start_state
        self.type_username = self.get_type_username_action(new_state)
        new_state = self.type_username.end_state
        self.submit_user = self.get_submit_action(new_state)
        new_state = self.submit_user.end_state
        self.password = self.get_type_password_action(new_state)
        self.submit = self.get_submit_action(new_state)

        if self.click_login is not None:
            actions.append(self.click_login)
        actions.append(self.click_login)
        actions.append(self.submit_user)
        actions.append(self.password)
        actions.append(self.submit)
        test = Test(name="Login Test %s" % self.url, actions = actions)
        test.save()
        return test


    def get_submit_action(self, state):
        submit_button = self.find_input(state, [ElementType.SUBMIT])
        if submit_button is None:
            raise Exception("Can't find submit_button ")
        submit = action_builder.get_click_action(submit_button,state, state)
        submit.execute(self.driver, self.config)
        new_state = state_builder.get_new_state(self.driver,state)
        new_state.save()
        submit.end_state = new_state
        return submit

    def get_type_password_action(self, state):
        password_field = self.find_input(state, [ElementType.PASSWORD])
        if password_field is None:
            raise Exception("Can't find password field")
        type_password = action_builder.get_sendkeys_action(password_field,state, state)
        type_password.execute(self.driver,self.config)
        new_state = state_builder.get_new_state(self.driver,state)
        new_state.save()
        type_password.end_state = new_state
        return type_password

    def get_type_username_action(self, state):
        username_field = self.find_input(state, [ElementType.USERNAME, ElementType.LOGIN])
        if username_field is None:
            raise Exception("Can't find username field")
        send_username = action_builder.get_sendkeys_action(username_field,state, state)
        send_username.execute(self.driver,self.config)
        new_state = state_builder.get_new_state(self.driver,state)
        new_state.save()
        send_username.end_state = new_state
        return send_username

    def get_click_login_action(self, state):
        username_field = self.find_input(state, [ElementType.USERNAME, ElementType.LOGIN])
        if username_field is not None:
            return None
        else:
            click_login = action_builder.get_click_action(self.login_link,self.start_state, self.end_state)
            click_login.execute(self.driver, self.config)
            new_state = state_builder.get_new_state(self.driver,state)
            new_state.save()
            click_login.end_state = new_state
            click_login.save()
            return click_login

    def find_input(self, start_state, element_types):
        for element in start_state.elements:
            if "<input" in element.html:
                field = WebElement(self.driver, element.locators)
                field.highlight(color="green")
                if field.is_editable() and element.type in element_types:
                    return element
        # raise Exception("Could find %s field in state : %s" % (element_types,start_state.id))
        return None

    def find_submit(self, start_state, element_types):
        for element in start_state.elements:
            if element.type in element_types:
                field = WebElement(self.driver, element.locators)
                if field.is_clickable():
                    return element
        raise Exception("Could find %s field in state : %s" % (element_types,start_state.id))

    def find_login_link(self, start_state):
        for element in start_state.elements:
            if element.type == ElementType.LOGIN:
                field = WebElement(self.driver, element.locators)
                if field.is_clickable():
                    return element
        return None


    def get_login_action(self):

        command1 = Command(command=Command.SENDKEYS, element=self.username, config_key=ElementType.USERNAME)
        command2 = Command(command=Command.SENDKEYS, element=self.password, config_key=ElementType.PASSWORD)
        command3 = Command(command=Command.CLICK, element=self.submit)

        action = Action(name="Login %s" % self.start_state.url, steps=[command1,command2,command3], start_state=self.start_state)

        response = action.execute(self.driver,self.config)
        if response.passed and not self.start_state.is_state_present(self.driver):
            print "assuming login was successful because the inputs are no longer present"
            self.end_state = state_builder.get_current_state(self.driver)
            self.end_state.save()
            action.end_state = self.end_state
            action.save()
            return action
        else:
            raise Exception("Could not generate login action")


    def get_logout_action(self):

        command1 = Command(command=Command.SENDKEYS, element=self.username, config_key=ElementType.USERNAME)
        command2 = Command(command=Command.SENDKEYS, element=self.password, config_key=ElementType.PASSWORD)
        command3 = Command(command=Command.CLICK, element=self.submit)

        action = Action(name="Login %s" % self.start_state.url, steps=[command1,command2,command3], start_state=self.start_state)

        response = action.execute(self.driver,self.config)
        if response.passed and not self.start_state.is_state_present(self.driver):
            print "assuming login was successful because the state is no longer present"
            self.end_state = state_builder.get_current_state(self.driver)
            self.end_state.save()
            action.end_state = self.end_state
            action.save()
            return action
        else:
            raise Exception("Could not generate login action")
