from datetime import datetime

class Employee(object):
    
    self.call = None
    self.rank = None

    def take_call(self, call):
        self.call = call

    def end_call(self):
        self.call = None

    def is_available(self):
        return self.call is None

    def scale_up(self):
        self.call.rank -= 1
        # send call to queue
        self.end_call()


class Director(Employee):

    def __init__(self, _id):
        self.rank = 0
        self.id = _id

class Manager(Employee):

    def __init__(self, _id):
        self.rank = 1
        self.id = _id

class Respondent(Employee):
    
    def __init__(self, _id):
        self.rank = 2
        self.id = _id

class Call(object):

    def __init__(self, caller):
        self.start_time = datetime.now()
        self.end_time = None
        self.caller = caller
        self.employee = None
        self.rank = 2

    def employee_on_line(self, employee):
        self.employee = employee

    def end_call(self):
        self.end_time = datetime.now()

    def duration(self):
        if self.end_time is None:
            return (datetime.now() - self.start_time).total_seconds() # in seconds
        else:
            return (self.end_time - self.start_time).total_seconds() # in seconds

class CallCenter(object):

    def __init__(self, num_respondents=50, num_managers=10, num_directors=2):
        self.employees   = [[ Director(i) for i in range(num_directors) ], 
                            [ Manager(num_directors + i) for i in range(num_managers) ],
                            [ Respondent(num_directors + num_managers + i) for i in range(num_respondents) ]]
        self.call_database = dict() # organized by time
        self.call_queues = [list(), list(), list()]

    def dispatch_call(self, caller):
        call = Call(caller)
        self.call_database[call.start_time] = call
        self._dispatch_call(self, call)

    def _dispatch_call(self, call):
        employee = get_available_employee(call)
        if employee is not None:
            employee.take_call(call)
            call.employee_on_line(employee)
        else:
            self.call_queues[call.rank] = call

    def get_available_employee(call):
        pass

    # look for available employees for each call queue, run this method constantly
    def assign_call(employee):
        pass





