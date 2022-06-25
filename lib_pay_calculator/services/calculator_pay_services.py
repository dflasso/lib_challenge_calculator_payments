from datetime import datetime, timedelta
from abc import ABC, abstractmethod
from typing import Any, List
from lib_pay_calculator.exceptions.illegal_arguments_exception import IllegalArgumentsError

from lib_pay_calculator.models import EmployeePayment,  EmployeeDaysWorked
from lib_pay_calculator.models.setting_day_model import SettingDay


ONE_MINUTE = timedelta(minutes=1)

class ICalculatorPayService(ABC):
    """
    Interfaces that define funtions to calculate payments to employee
    """
    @abstractmethod
    def calculate(self, data, settings) -> Any:
        pass



class CalculatorPayService(ICalculatorPayService):
    """
    Implementation of service for to calculate payment to Employee
    """
    def calculate(self, data, lts_settings) -> EmployeePayment:
        """
        :type data: lib_test.models.EmployeePayment
        :param data: Object with necesary fields for calculation

        :type lts_settings: List of lib_test.models.SettingDay
        :param lts_settings: list with items that has params for get amount 
        """
        self.__check_types_arguments(data=data, lts_settings=lts_settings)
        
        for item in data: 
            for day_worked in item.days_worked:
                if not isinstance(day_worked, EmployeeDaysWorked):
                    raise IllegalArgumentsError(message=f"Unexpected type of day_worked {type(day_worked)}. Type expected lib_test.models.EmployeeDaysWorked")
                
                for setting in lts_settings:
                    if day_worked.day_abbreviated == setting.abbreviated_day_name:
                        day_worked = self.__get_amount_pay_of_day(day_worked=day_worked, setting=setting)
        
        return data
            

    def __check_types_arguments(self, data, lts_settings):
        if not isinstance(data, List):
            raise IllegalArgumentsError(message=f"Unexpected type of data {type(data)}. Type expected List")
        
        for item in data: 
            if not isinstance(item, EmployeePayment):
                raise IllegalArgumentsError(message=f"Unexpected type item of data {type(item)}. Type expected lib_test.models.EmployeePayment")
            if len(item.days_worked) < 1: 
                raise IllegalArgumentsError(message=f"days_worked is Empty")

        if len(lts_settings) < 1: 
            raise IllegalArgumentsError(message=f"lts_settings is Empty")
        
        for setting in lts_settings:
            if not isinstance(setting, SettingDay):
                raise IllegalArgumentsError(message=f"Unexpected type of setting {type(setting)}. Type expected lib_test.models.SettingDay")


    def __get_amount_pay_of_day(self, day_worked, setting):
        start_hour_worked = "1/1/22 " + day_worked.start_hour
        end_hour_worked =  "1/1/22 "  + day_worked.end_hour     

        start_hour_worked =  datetime.strptime(start_hour_worked, '%d/%m/%y %H:%M')
        end_hour_worked = datetime.strptime(end_hour_worked, '%d/%m/%y %H:%M')
        
        day_worked.pay_amount = 0.00
        
        for schedule in setting.work_schedules:
            if schedule.from_hour <= start_hour_worked <= schedule.to_hour:
                if end_hour_worked <= schedule.to_hour:
                    day_worked.pay_amount += self.__calculate_total_hours_worked(end_hour_worked=end_hour_worked, 
                                                                                 start_hour_worked=start_hour_worked, 
                                                                                 value_by_hour=schedule.value)
                else :
                    day_worked.pay_amount += self.__calculate_total_hours_worked(end_hour_worked=schedule.to_hour, 
                                                                                 start_hour_worked=start_hour_worked, 
                                                                                 value_by_hour=schedule.value)
                    start_hour_worked = schedule.to_hour + ONE_MINUTE
        return day_worked

    def __calculate_total_hours_worked(self, end_hour_worked, start_hour_worked, value_by_hour):
        total_hours_worked  = end_hour_worked - start_hour_worked
        total_hours_worked = total_hours_worked.seconds / 3600 
        total_hours_worked = round(total_hours_worked)
        return total_hours_worked * value_by_hour