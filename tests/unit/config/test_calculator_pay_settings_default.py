from typing import List
import unittest

from lib_pay_calculator.config import CalculatorPaySettingsDefault
from lib_pay_calculator.models import SettingDay


class TestCalculatorPaySettingsDefault(unittest.TestCase):
    
    def test_build_calculator_pay_handler(self):
        """
        Unit test create a calculator_pay_handler with default values
        """
        calculator_pay_builder = CalculatorPaySettingsDefault()
        calculator_pay_settings = calculator_pay_builder.calculator_pay_settings

        self.assertTrue(isinstance(calculator_pay_settings, List), msg=f"type obtained: {type(calculator_pay_settings)},type expected List")
        self.assertTrue(len(calculator_pay_settings) == 7)
        self.assertTrue( isinstance(calculator_pay_settings[0], SettingDay ))
        self.assertEqual(calculator_pay_settings[0].abbreviated_day_name, "MO" )
        self.assertTrue( isinstance( calculator_pay_settings[0].work_schedules, List ) )
        self.assertTrue(len(calculator_pay_settings[0].work_schedules) >= 3)
        self.assertEqual(calculator_pay_settings[0].work_schedules[0].value, 25.0 )
