
class SettingDay(object):
    """
    DTO with necesary fields for to do calculation of payments
    """
        

    @property
    def day_name(self):
        return self.__day_name


    @day_name.setter
    def day_name(self, value = ""):
        pass
    
    @property
    def abbreviated_day_name(self):
        return self.__abbreviated_day_name


    @abbreviated_day_name.setter
    def abbreviated_day_name(self, value = ""):
        pass

    @property
    def work_schedules(self):
        return self.__work_schedules

    @work_schedules.setter
    def work_schedules(self, work_schedules):
        pass
