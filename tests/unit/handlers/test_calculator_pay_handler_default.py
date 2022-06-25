from typing import List
import unittest

from lib_pay_calculator.handlers.calculator_pay_handler_default import CalculatorPayHandler


class TestCalculatorPayHandler(unittest.TestCase):
    
    def test_one_employee(self):
        hanlder = CalculatorPayHandler()

        input = ["RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00"]

        hanlder.payments = input

        self.assertTrue( isinstance(hanlder.payments, List) )
        self.assertTrue( len(hanlder.payments) == 1 )

        self.assertEqual( hanlder.payments[0] , "The amount to pay RENE is: 215.0 USD" )
    
    def test_two_employees(self):
        hanlder = CalculatorPayHandler()

        input = ["RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00",
                 "ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00"]

        hanlder.payments = input

        self.assertTrue( isinstance(hanlder.payments, List) )
        self.assertTrue( len(hanlder.payments) == 2 )

        self.assertEqual( hanlder.payments[0] , "The amount to pay RENE is: 215.0 USD" )
        self.assertEqual( hanlder.payments[1] , "The amount to pay ASTRID is: 85.0 USD" )