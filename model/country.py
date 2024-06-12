#!/usr/bin/python3
from base import Base

class Country(Base):
    """
    A class representing a country.
    """

    def __init__(self, name, id=None, states=None):
        self.name = name
        self.states = states if states else []

    def add_state(self, state):
        if state not in self.states:
            self.states.append(state)
        else:
            print(f"{state} is already in the list of states")

    def remove_state(self, state):
        if state in self.states:
            self.states.remove(state)
        else:
            print(f"{state} not found in states")

    def update(self, new_name):
        self.name = new_name

    def delete(self):
        pass

    def __str__(self):
        states_str = ', '.join(self.states)
        return f"Country(ID: {self.id}, Name: {self.name}, States: [{states_str}])"