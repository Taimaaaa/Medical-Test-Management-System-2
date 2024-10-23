class MedicalTest:
    def __init__(self, testName, range, range2, unit,day,hour,minute):
        self.testName = testName
        self.range = range
        self.range2 = range2
        self.unit = unit
        self.day = day
        self.hour = hour
        self.minute = minute

    # Getters
    def get_testName(self):
        return self.testName

    def get_range(self):
        return self.range

    def get_range2(self):
        return self.range2

    def get_unit(self):
        return self.unit
    def get_day(self):
        return self.day
    def get_hour(self):
        return self.hour
    def get_minute(self):
        return self.minute


    # Setters
    def set_testName(self, testName):
        self.testName = testName

    def set_range(self, range):
        self.range = range

    def set_range2(self, range2):
        self.range2 = range2

    def set_unit(self, unit):
        self.unit = unit
    def set_day(self, day):
        self.day = day
    def set_hour(self, hour):
        self.unit = hour
    def set_minute(self, minute):
        self.unit = minute


    # Existing method
    def rangeOrder(self):
        if self.range > self.range2 and self.range2 > 0:
            temp = self.range
            self.range = self.range2
            self.range2 = temp
