class SettingSchedule(object):
    """
    DTO with fields necesaries for determine value of hour
    """

    @property 
    def from_hour(self):
        return self.__from_hour

    @from_hour.setter
    def from_hour(self, value):
        pass


    @property 
    def to_hour(self):
        return self.__to_hour

    @to_hour.setter
    def to_hour(self, value):
        pass


    @property 
    def value(self):
        return self.__value

    @value.setter
    def value(self, _value):
        pass