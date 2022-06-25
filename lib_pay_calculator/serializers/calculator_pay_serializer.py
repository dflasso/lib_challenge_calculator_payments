from abc import ABC, abstractmethod
from typing import Any

class ICalculatorPaySerializer(ABC):
    
    """
    Interfaces that define funtions to serialize inputs of payments calculation
    """
    
    @property
    @abstractmethod
    def data(self) -> Any:
        pass

    @data.setter
    @abstractmethod
    def data(self, raw_data) -> None:
        pass