from abc import ABC, abstractmethod
from typing import List


class ICalculatorPaySettingsBuilder(ABC):
    """
    The Builder interface specifies methods for creating a service 
    that handle calcultion of payments.
    """
    
    @property
    @abstractmethod
    def calculator_pay_settings(self) -> List:
        pass

    @calculator_pay_settings.setter
    @abstractmethod
    def calculator_pay_settings(self, parameters) -> None:
        """
        :type parameters: List of config.CalculatorPayParams
        :param  parameters: ICalculatorPayHandler use this parameters for calculate payments
        """
        pass