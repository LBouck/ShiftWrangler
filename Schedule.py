from Shift import *
from Employee import *


class Schedule:
    def __init__(self):
        self.employees = []

        # contains the head of the shift linked list for the day
        self.first_shifts = {"Monday":None, "Tuesday":None, "Wednesday":None,\
        "Thursday":None, "Friday":None,"Saturday":None, "Sunday":None}
        self.permutations = 1

    def add_employee(employee):
        if employee in self.employees:
            return False
        self.employees.add(employee)
        return True

    def 
