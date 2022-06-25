from typing import List

from lib_pay_calculator.exceptions.error_model import ErrorModel
from lib_pay_calculator.exceptions.illegal_arguments_exception import IllegalArgumentsError

class SettingDay(object):
    """
    DTO with necesary fields for to do calculation of payments
    """
        
    @property
    def day_name(self):
        return self.__day_name

    @day_name.setter
    def day_name(self, value = ""):
        if not isinstance(value, str):
            error_detail = ErrorModel(message="unexpected type of day_error", field="day_error", obj="CalculatorPayParams")
            raise IllegalArgumentsError(message="illegal argument 'day_name'", sub_errors=[error_detail])

        if value.replace(" ", " ") == "":
            error_detail = ErrorModel(message="day_error is empty", field="day_error", obj="CalculatorPayParams")
            raise IllegalArgumentsError(message="illegal argument 'day_name'", sub_errors=[error_detail])

        self.__day_name = value
    
    @property
    def abbreviated_day_name(self):
        return self.__abbreviated_day_name


    @abbreviated_day_name.setter
    def abbreviated_day_name(self, value = ""):
        if not isinstance(value, str):
            error_detail = ErrorModel(message="unexpected type of abbreviated_day_name", field="abbreviated_day_name", obj="CalculatorPayParams")
            raise IllegalArgumentsError(message="illegal argument 'abbreviated_day_name'", sub_errors=[error_detail])

        if value.replace(" ", " ") == "":
            error_detail = ErrorModel(message="abbreviated_day_name is empty", field="abbreviated_day_name", obj="CalculatorPayParams")
            raise IllegalArgumentsError(message="illegal argument 'abbreviated_day_name'", sub_errors=[error_detail])

        self.__abbreviated_day_name = value

    @property
    def work_schedules(self):
        return self.__work_schedules

    @work_schedules.setter
    def work_schedules(self, work_schedules):
        """
        :type schedule: models.SettingSchedule
        """
        if not isinstance(work_schedules, List):
            error_detail = ErrorModel(message="unexpected type of work_schedules", field="work_schedules", obj="CalculatorPayParams")
            raise IllegalArgumentsError(message="illegal argument 'work_schedules'", sub_errors=[error_detail])

        self.__work_schedules = work_schedules
