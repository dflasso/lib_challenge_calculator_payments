from abc import ABC, abstractmethod
from typing import Any

class ICalculatorPayDeserializer(ABC):
    """
    Interfaces that define funtions to deserialize inputs of payments calculation
    """

    @abstractmethod
    def parse(self, processed_data) -> Any:
        pass