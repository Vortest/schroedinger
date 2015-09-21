from app import state_builder
from app.element_comparer import ElementComparer
from models.state import State

home_states = State.objects(url="https://www.bluemodus.com/home")[:1]
for state in home_states:
    print state.id

who_state = State.objects(url="https://www.bluemodus.com/who-we-work-with").all()
print who_state.id


