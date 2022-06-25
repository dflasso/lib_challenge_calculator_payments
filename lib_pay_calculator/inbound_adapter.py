from io import TextIOWrapper
import base64
import re

from lib_pay_calculator.exceptions.bad_formart_exception import BadFormatError
from lib_pay_calculator.handlers.calculator_pay_handler_default import CalculatorPayHandler


def from_list_str(list_employees : list[str]) -> list[str]:
    hanlder = CalculatorPayHandler()
    hanlder.payments = list_employees
    
    return hanlder.payments 


def from_base64( file_content : str):
    list_employees = []
    content_bytes = None
    try:
        content_bytes  = base64.b64decode(file_content)
    except Exception as error:
        raise BadFormatError(message=error, format_expected='data in base64')

    list_employees = from_bytes(file_content=content_bytes)
    return list_employees

def from_bytes( file_content : bytes) -> list[str]:
    
    list_employees_str = ""
    try:
        list_employees_str = file_content.decode("utf-8")
    except Exception as error:
        raise BadFormatError(message=error, format_expected='array of bytes')
    
    list_employees = list_employees_str.split("\n")
    
    return from_list_str(list_employees=list_employees)


def from_base64_to_console(file_content : str):
    list_employees = from_base64(file_content=file_content)

    summary = ""
    for employee_payment in list_employees:
        summary += f"{employee_payment}\n"

    print(summary)

def from_txt(file : TextIOWrapper):
    list_employees_str = file.readlines()
    clean_data = []
    for items in list_employees_str:
        items = re.sub('[^A-Za-z0-9 -:=,]+', '', items)
        clean_data.append(items)

    return from_list_str(list_employees=clean_data)