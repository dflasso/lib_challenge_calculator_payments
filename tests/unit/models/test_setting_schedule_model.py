from datetime import datetime
import unittest


from lib_pay_calculator.exceptions.illegal_arguments_exception import IllegalArgumentsError
from lib_pay_calculator.models.setting_schedule_model import SettingSchedule


class TestSettingSchedule(unittest.TestCase):
    
    def test_validations_from_hour_field(self):
        schedule = SettingSchedule()

        with self.assertRaises(IllegalArgumentsError): schedule.from_hour = 0
        with self.assertRaises(IllegalArgumentsError): schedule.from_hour = "0"

        schedule.from_hour = datetime(year=1000, month=1, day=1, hour=1, minute=1, second=1)

        self.assertEqual(schedule.from_hour ,  datetime(year=1000, month=1, day=1, hour=1, minute=1, second=1))        
    
    def test_validations_to_hour_field(self):
        schedule = SettingSchedule()

        # type of data validation
        with self.assertRaises(IllegalArgumentsError): schedule.to_hour = 0
        with self.assertRaises(IllegalArgumentsError): schedule.to_hour = "0"
        
        schedule.to_hour = datetime(year=1000, month=1, day=1, hour=1, minute=1, second=2)

        self.assertEqual(schedule.to_hour ,  datetime(year=1000, month=1, day=1, hour=1, minute=1, second=2))

    def test_validations_value_field(self):
        schedule = SettingSchedule()

        with self.assertRaises(IllegalArgumentsError): schedule.value = True
        with self.assertRaises(IllegalArgumentsError): schedule.value = "0"

        schedule.value = 2.0

        self.assertEqual(schedule.value ,  2.0)