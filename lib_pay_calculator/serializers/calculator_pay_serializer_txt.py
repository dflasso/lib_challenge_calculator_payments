

from typing import List

from lib_pay_calculator.exceptions import IllegalArgumentsError
from lib_pay_calculator.exceptions.bad_formart_exception import BadFormatError
from lib_pay_calculator.models import EmployeePayment

from .calculator_pay_serializer import ICalculatorPaySerializer
from .calculator_pay_deserializer import ICalculatorPayDeserializer

class CalculatorPaySerializerTxt(ICalculatorPaySerializer, ICalculatorPayDeserializer):
    
    """
    Implementation that define funtions to serialize outputs of payments calculation
    """    
    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, raw_data) -> None:
        if not isinstance(raw_data, List):
            raise IllegalArgumentsError(message=f"Unexpected type of 'raw_data', It is: {type(raw_data)}. Expected type: List ")

        lts_employes_payment = []
        for row in raw_data:
            employee_name, params_for_payment = self.__handle_row_of_file(row)
            emp_payment = EmployeePayment(name=employee_name, days_worked=params_for_payment)
            lts_employes_payment.append(emp_payment)
        
        self.__data = lts_employes_payment


    def parse(self, processed_data : list):
        summary_payments = []
        for item in processed_data:
            if not isinstance(item, EmployeePayment):
                raise IllegalArgumentsError(message=f"Unexpected type of item in processed_data: {type(item)}. Type expected lib_test.models.EmployeePayment")

            total_payment = 0.0
            for day_worked in item.days_worked:
                total_payment += day_worked.pay_amount
            summary_payments.append(f"The amount to pay {item.name} is: {total_payment} USD")
        
        return summary_payments

    def __handle_row_of_file(self,row):
        info = row.split("=")

        if len(info) < 2: 
            raise BadFormatError(message=f"Bad format in Line: {info}", format_expected="NAME=MO10:00-12:00,")
        
        employee_name = info[0]
        params_for_payment = self.__handle_payment_info( info[1] )

        return employee_name, params_for_payment

    def __handle_payment_info(self , payment_info):
        days_worked = payment_info.split(",")

        params_for_payment = []
        for day_worked in days_worked:
            hours_worked = day_worked[2:].split("-")
            
            if len(hours_worked) != 2:
                raise BadFormatError(message=f"Bad format with hours worked day {day_worked[0:2]}, hours {hours_worked}", format_expected="NAME=MO10:00-12:00,")

            param_for_payment = {
                "day_abbreviated": day_worked[0:2],
                "start_hour": hours_worked[0],
                "end_hour": hours_worked[1]
            }

            params_for_payment.append(param_for_payment)
        
        return params_for_payment