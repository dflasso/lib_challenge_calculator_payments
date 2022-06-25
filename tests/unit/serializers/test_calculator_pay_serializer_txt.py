from typing import List
import unittest

from lib_pay_calculator.exceptions.illegal_arguments_exception import IllegalArgumentsError
from lib_pay_calculator.models.emp_payment_model import EmployeePayment
from lib_pay_calculator.serializers.calculator_pay_serializer_txt import CalculatorPaySerializerTxt


class TetsCalculatorPaySerializerTxt(unittest.TestCase):
    

    def test_serializing_input(self):
        serializer = CalculatorPaySerializerTxt()
        input = ["RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00"]

        with self.assertRaises(IllegalArgumentsError): serializer.data = "RENE"
        
        serializer.data = input

        self.assertTrue( isinstance(serializer.data , List) )
        self.assertTrue( len(serializer.data) == 1 )

        self.assertTrue( isinstance(serializer.data[0], EmployeePayment) )
        self.assertEqual( serializer.data[0].name, "RENE"  )

        self.assertTrue( isinstance(serializer.data[0].days_worked , List) )
        self.assertTrue( len(serializer.data[0].days_worked) == 5 )

        self.assertEqual( serializer.data[0].days_worked[0].day_abbreviated, "MO"  )
        self.assertEqual( serializer.data[0].days_worked[0].start_hour, "10:00"  )
        self.assertEqual( serializer.data[0].days_worked[0].end_hour, "12:00"  )

        self.assertEqual( serializer.data[0].days_worked[4].day_abbreviated, "SU"  )
        self.assertEqual( serializer.data[0].days_worked[4].start_hour, "20:00"  )
        self.assertEqual( serializer.data[0].days_worked[4].end_hour, "21:00"  )