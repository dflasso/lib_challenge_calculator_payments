import datetime
from typing import List

from lib_pay_calculator.exceptions import IllegalArgumentsError
from lib_pay_calculator.models import SettingDay, SettingSchedule
from .calculator_pay_settings_builder import ICalculatorPaySettingsBuilder

DAYS = ( "MO", "TU", "WE", "TH", "FR" )

WEEKEND_DAY = ("SA", "SU")



MONDAY_TO_FRIDAY_DEFAULT_VALUES = (  
    (datetime.datetime(year=2022, month=1, day=1,hour=0,minute=1 ), datetime.datetime(year=2022, month=1, day=1,hour=9,minute=0 ), 25.0), 
    (datetime.datetime(year=2022, month=1, day=1,hour=9,minute=1 ), datetime.datetime(year=2022, month=1, day=1,hour=18,minute=0 ),  15.0),  
    (datetime.datetime(year=2022, month=1, day=1,hour=18,minute=1 ), datetime.datetime(year=2022, month=1, day=1,hour=23,minute=59, second=59),20.0)
)

WEEKEND_DEFAULT_VALUE = (
    (datetime.datetime(year=2022, month=1, day=1,hour=0,minute=1 ), datetime.datetime(year=2022, month=1, day=1,hour=9,minute=0 ), 30.0), 
    (datetime.datetime(year=2022, month=1, day=1,hour=9,minute=1 ), datetime.datetime(year=2022, month=1, day=1,hour=18,minute=0 ),  20.0),  
    (datetime.datetime(year=2022, month=1, day=1,hour=18,minute=1 ), datetime.datetime(year=2022, month=1, day=1,hour=23,minute=59, second=59), 25.0)
)

class CalculatorPaySettingsDefault(ICalculatorPaySettingsBuilder):
    """
    The Concrete Builder classes follow the Builder interface and provide
    specific implementations with default settings.
    """

    def __init__(self) -> None:
        super().__init__()
        self.calculator_pay_settings = self.__build_settings()

    @property
    def calculator_pay_settings(self) -> List:
        return self.__calculator_pay_settings
        

    @calculator_pay_settings.setter
    def calculator_pay_settings(self, parameters) -> None:
        if not isinstance(parameters, List):
            raise IllegalArgumentsError(message=f"Unexpected type of parameters: {type(parameters)}")

        for parameter in parameters:
            if not isinstance(parameter, SettingDay):
                raise IllegalArgumentsError(message=f"Unexpected item in parameters of type {type(parameter)}")

        self.__calculator_pay_settings = parameters
    
    def __build_settings(self):
        settings = []

        setting = None
        for day_week in DAYS:
            setting = self.__build_setting(day_week, MONDAY_TO_FRIDAY_DEFAULT_VALUES)
            settings.append(setting)
        
        for day_weekend in WEEKEND_DAY:
            setting = self.__build_setting(day_weekend, WEEKEND_DEFAULT_VALUE)
            settings.append(setting)
        
        return settings
    
    def __build_setting(self, abbreviated_day_name, work_schedules):
        setting = SettingDay()
        setting.abbreviated_day_name = abbreviated_day_name

        settings_schedule = []
        for schedule in work_schedules:
            setting_schedule = SettingSchedule()
            setting_schedule.from_hour = schedule[0]
            setting_schedule.to_hour = schedule[1]
            setting_schedule.value = schedule[2]

            settings_schedule.append(setting_schedule)

        setting.work_schedules = settings_schedule

        return setting
