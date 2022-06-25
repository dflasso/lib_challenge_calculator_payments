
class EmployeeDaysWorked(object):
    
    @property
    def day_abbreviated(self):
        return self.__day_abbreviated

    @day_abbreviated.setter
    def day_abbreviated(self, abbreviated):
        self.__day_abbreviated = abbreviated
    
    @property
    def start_hour(self):
        return self.__start_hour

    @start_hour.setter
    def start_hour(self, hour):
        self.__start_hour = hour

    @property
    def end_hour(self):
        return self.__end_hour

    @end_hour.setter
    def end_hour(self, hour):
        self.__end_hour = hour

    @property
    def day_abbreviated(self):
        return self.__day_abbreviated

    @day_abbreviated.setter
    def day_abbreviated(self, abbreviated):
        self.__day_abbreviated = abbreviated
    
    @property
    def pay_amount(self):
        return self.__pay_amount
    
    @pay_amount.setter
    def pay_amount(self, amount):
        self.__pay_amount = amount
