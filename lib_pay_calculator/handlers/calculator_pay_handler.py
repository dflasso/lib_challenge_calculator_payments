from abc import ABC, abstractmethod
from typing import Any

from lib_pay_calculator.config import ICalculatorPaySettingsBuilder
from lib_pay_calculator.serializers import ICalculatorPaySerializer
from lib_pay_calculator.serializers.calculator_pay_deserializer import ICalculatorPayDeserializer
from lib_pay_calculator.services import ICalculatorPayService


class ICalculatorPayHandler(ABC):

    """
    Interfaces that define funtions to handle inputs and outputs of librery
    """

    @abstractmethod
    def setup(self, builder : ICalculatorPaySettingsBuilder, calculator_service: ICalculatorPayService) -> None:
        """
        Build a object with settings for calculation payments
        """
        pass

    @abstractmethod
    def import_data_setup(self, serializer: ICalculatorPaySerializer) -> None:
        pass

    @abstractmethod
    def export_data_setup(self, serializer: ICalculatorPayDeserializer) -> None:
        pass
    

    @property
    @abstractmethod
    def payments(self) -> Any:
        pass

    @payments.setter
    @abstractmethod
    def payments(self, raw_data) -> None:
        pass

    @property
    @abstractmethod
    def settings(self) -> Any:
        pass

    @settings.setter
    @abstractmethod
    def settings(self, values) -> None:
        pass