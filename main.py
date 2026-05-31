from lessons.variables import variable_demo
from lessons.type_annotations import type_demo 
from lessons.constants import constants_demo
from lessons.functions import show_date, greet, add
from lessons.classes import Car 

# variable_demo()
# type_demo()
# constants_demo()
# show_date()
# greet("alice")
# greet("Bob")
# print(add(2.1, 1.2))


volvo: Car = Car("Volvo", 200)
print(volvo)
volvo.drive()
volvo.get_info()