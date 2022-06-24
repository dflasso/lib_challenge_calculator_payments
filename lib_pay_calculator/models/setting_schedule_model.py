from datetime import datetime

from lib_pay_calculator.exceptions import ErrorModel, IllegalArgumentsError


class SettingSchedule(object):
    """
    DTO with fields necesaries for determine value of hour
    """

    @property 
    def from_hour(self):
        return self.__from_hour

    @from_hour.setter
    def from_hour(self, value):
        if not isinstance(value, datetime):
            error_detail = ErrorModel(message="unexpected type of from_hour", field="from_hour", obj="CalculatorPayParams")
            raise IllegalArgumentsError(message="illegal argument 'from_hour'", sub_errors=[error_detail])

        self.__from_hour = value


    @property 
    def to_hour(self):
        return self.__to_hour

    @to_hour.setter
    def to_hour(self, value):
        if not isinstance(value, datetime):
            error_detail = ErrorModel(message="unexpected type of to_hour", field="from_hour", obj="CalculatorPayParams")
            raise IllegalArgumentsError(message="illegal argument 'to_hour'", sub_errors=[error_detail])

        self.__to_hour = value


    @property 
    def value(self):
        return self.__value

    @value.setter
    def value(self, _value):
        if not isinstance(_value, float):
            error_detail = ErrorModel(message="unexpected type of _value", field="_value", obj="CalculatorPayParams")
            raise IllegalArgumentsError(message="illegal argument '_value'", sub_errors=[error_detail])

        if _value < 0.00:
            error_detail = ErrorModel(message="_value must be more that 0", field="_value", obj="CalculatorPayParams")
            raise IllegalArgumentsError(message="illegal argument '_value'", sub_errors=[error_detail])

        self.__value = _value