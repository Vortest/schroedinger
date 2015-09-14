from app import state_builder
from models.action import Action
from models.command import Command
def get_click_action(element, start_state, end_state):
    command = Command(element=element,command=Command.CLICK)
    action = Action(name="Click %s" % str(element), steps=[command],start_state=start_state,end_state=end_state)
    action.save()
    return action

def get_nav_action(url, end_state):
    command1 = Command(command=Command.NAVIGATE, params=url)
    action = Action(name="Get %s" % url, steps=[command1], start_state=state_builder.get_blank_state(), end_state=end_state)
    action.save()
    return action