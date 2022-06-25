

from lib_pay_calculator.config import CalculatorPaySettingsDefault
from lib_pay_calculator.config.calculator_pay_settings_builder import ICalculatorPaySettingsBuilder
from lib_pay_calculator.exceptions.illegal_arguments_exception import IllegalArgumentsError
from lib_pay_calculator.serializers import ICalculatorPayDeserializer,  ICalculatorPaySerializer, CalculatorPaySerializerTxt
from lib_pay_calculator.services import ICalculatorPayService,  CalculatorPayService
from .calculator_pay_handler import ICalculatorPayHandler


class CalculatorPayHandler(ICalculatorPayHandler):

    __settings = []
    __serializer : ICalculatorPaySerializer = None
    __deserializer : ICalculatorPayDeserializer = None
    __calulator_service : ICalculatorPayService = None

    def __init__(self) -> None:
        super().__init__()

        builderDefault = CalculatorPaySettingsDefault()
        calculator = CalculatorPayService()
        self.setup(builder=builderDefault, calculator_service=calculator)

        convert = CalculatorPaySerializerTxt()
        self.import_data_setup(serializer=convert)
        self.export_data_setup(deserializer=convert)
    

    def setup(self, builder : ICalculatorPaySettingsBuilder, calculator_service: ICalculatorPayService) -> None:
        if not isinstance(builder, ICalculatorPaySettingsBuilder):
            raise IllegalArgumentsError(message="illegal argument 'builder' isn't a implementation of ICalculatorPaySettingsBuilder")

        self.settings = builder.calculator_pay_settings
        self.__calulator_service = calculator_service


    def import_data_setup(self, serializer) -> None:
        self.__serializer = serializer


    def export_data_setup(self, deserializer) -> None:
        self.__deserializer = deserializer    

    @property
    def payments(self):
        processed_data = self.__calulator_service.calculate(data=self.__serializer.data, 
                                                            lts_settings=self.settings)
        return self.__deserializer.parse(processed_data=processed_data)

    @payments.setter
    def payments(self, raw_data) -> None:
        self.__serializer.data = raw_data

    @property
    def settings(self):
        return self.__settings

    @settings.setter
    def settings(self, values):
        self.__settings = values