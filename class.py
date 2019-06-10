class Human:
    
    def __init__(self, name, age = 0):
        self._name = name
        self._age = age
    
    def _say(self, text):
        print(text)

    def say_name(self):
        self._say(f"Hello, I'm {self._name}")

    def say_how_old(self):
        self._say(f"I'm {self._age}")

class Planet:
    
    def _init_(self, name, population = None):
        self.name = name
        self.population = population or []

    def add_human(self, human):
        print(f"Welcome to {self.name}, {human.name}!")
        self.population.append(human)


bob = Human("Bob", age = 29)
bob.say_name()
bob.say_how_old()

def extract_description(user_input):
    return "Open world championship."

def extract_date(user_input):
    return date(2019, 2, 21)

class Event:
    def __init__(self, description, event_date):
        self.description = description
        self.date = event_date

    def __str__(self):
        return f"Event \"{self.description}\" at {self.date}"
    
    @classmethod
    def from_string(cls, user_input):
        description = extract_description(user_input)
        date = extract_date(user_input)
        return cls(description, date)

from datetime import date

event_description = "Tell smth"
event_date = date.today()

event = Event(event_description, event_date)

print(event)

event = Event.from_string("Open world championship, 2019-02-21")

print(event)


