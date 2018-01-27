from datetime import time

class Shift: # Class for the shifts times needed to be filled
    def __init__(self):
        """ This provides the methods for tracking the amount of necessary
        employees of each level per shift. The day strings included in this
        class are for ease of use. Future implementations will include checks
        to prevent overlapping shifts in the case of manual input for
        availability."""
        # designates number of employees needed for a shift
        self.num_employees = {"Senior":(0,1), "Junior":(0,1)}
        self.available_employees = []
        self.day = ""
        self.start_time = None
        self.end_time = None

    def set_number_employees(self, level, min, max):
        if !(level in self.num_employees.keys()):
            return False
        if min > max:
            return False
        self.num_employees[level] = (int(min),int(max))
        return True

    def add_available_employee(employee):
        if employee in self.available_employees:
            return False
        self.available_employees.add(employee)

    def set_start_time(start):
        self.start_time = start

    def set_end_time(end):
        self.end_time = end
