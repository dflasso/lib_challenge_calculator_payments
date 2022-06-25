from typing import Dict, List

from lib_pay_calculator.exceptions import IllegalArgumentsError

from .emp_days_worked_model import EmployeeDaysWorked


class EmployeePayment(object):
    
    def __init__(self, name, days_worked) -> None:
        self.name = name
        self.days_worked = days_worked

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def days_worked(self):
        return self.__days_worked
    
    @days_worked.setter
    def days_worked(self, days):
        if not isinstance(days, List):
            raise IllegalArgumentsError(message=f"Unexpected type of days: {type(days)}. Expected List")            
        
        days_worked = []

        for day in days:
            
            if not isinstance(day, Dict):
                raise IllegalArgumentsError(message=f"Unexpected type of item days: {type(day)}. Expected Dict")            
            
            day_worked = EmployeeDaysWorked()

            if "day_abbreviated" in day:
                day_worked.day_abbreviated = day['day_abbreviated']
            
            if "start_hour" in day:
                day_worked.start_hour = day['start_hour']
            
            if "end_hour" in day:
                day_worked.end_hour = day['end_hour']

            days_worked.append(day_worked)


        self.__days_worked = days_worked