import unittest
from lib_pay_calculator.config.calculator_pay_settings_default import CalculatorPaySettingsDefault

from lib_pay_calculator.models.emp_payment_model import EmployeePayment
from lib_pay_calculator.services.calculator_pay_services import CalculatorPayService


class TestCalculatorPayService(unittest.TestCase):
    
    def test_calculate_two_hours_working_hours(self):
        param_for_payment = [ {
            "day_abbreviated": "MO",
            "start_hour" : "10:00",
            "end_hour" : "12:00"
            }]
        
        emp_payment = EmployeePayment(name="RENE", days_worked=param_for_payment)

        settings = CalculatorPaySettingsDefault()

        calculator = CalculatorPayService()

        lst_employees_payment = calculator.calculate(data=[emp_payment], lts_settings=settings.calculator_pay_settings)

        self.assertEqual(lst_employees_payment[0].days_worked[0].pay_amount, 30.00)
    
    def test_calculate_two_hours_early_morning(self):
        param_for_payment = [ {
            "day_abbreviated": "MO",
            "start_hour" : "6:00",
            "end_hour" : "9:00"
            }]
        
        emp_payment = EmployeePayment(name="RENE", days_worked=param_for_payment)

        settings = CalculatorPaySettingsDefault()

        calculator = CalculatorPayService()

        lst_employees_payment = calculator.calculate(data=[emp_payment], lts_settings=settings.calculator_pay_settings)

        self.assertEqual(lst_employees_payment[0].days_worked[0].pay_amount, 75.00)
    
    def test_calculate_two_hours_night_time(self):
        param_for_payment = [ {
            "day_abbreviated": "MO",
            "start_hour" : "20:00",
            "end_hour" : "21:00"
            }]
        
        emp_payment = EmployeePayment(name="RENE", days_worked=param_for_payment)

        settings = CalculatorPaySettingsDefault()

        calculator = CalculatorPayService()

        lst_employees_payment = calculator.calculate(data=[emp_payment], lts_settings=settings.calculator_pay_settings)

        self.assertEqual(lst_employees_payment[0].days_worked[0].pay_amount, 20.00)
    
    def test_calculate_nine_hours_all_day(self):
        param_for_payment = [ {
            "day_abbreviated": "MO",
            "start_hour" : "8:00",
            "end_hour" : "19:00"
            }]
        
        emp_payment = EmployeePayment(name="RENE", days_worked=param_for_payment)

        settings = CalculatorPaySettingsDefault()

        calculator = CalculatorPayService()

        lst_employees_payment = calculator.calculate(data=[emp_payment], lts_settings=settings.calculator_pay_settings)

        self.assertEqual(lst_employees_payment[0].days_worked[0].pay_amount, 180.00)