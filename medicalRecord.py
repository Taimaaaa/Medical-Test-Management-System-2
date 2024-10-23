
class MedicalRecord:
    def __init__(self,id,testname,year1,month1,day1,hour1,minute1,testValue,unit,status,year2,month2,day2,hour2,minute2):
        self.id = id
        self.testname = testname
        self.year1 = year1
        self.month1 = month1
        self.day1 = day1
        self.hour1 = hour1
        self.minute1 = minute1
        self.testValue = testValue
        self.unit = unit
        self.status = status
        self.year2 = year2
        self.month2 = month2
        self.day2 = day2
        self.hour2 = hour2
        self.minute2 = minute2

    def printMedicalRecord(self):
       if self.status == "completed":
        return f"{self.id}: {self.testname}, {self.year1}-{self.month1:02d}-{self.day1:02d} {self.hour1:02d}:{self.minute1:02d}, {self.testValue}, {self.unit}, {self.status}, {self.year2}-{self.month2:02d}-{self.day2:02d} {self.hour2:02d}:{self.minute2:02d}"
       if self.status == "pending" or self.status == "reviewed":
           return f"{self.id}: {self.testname}, {self.year1}-{self.month1:02d}-{self.day1:02d} {self.hour1:02d}:{self.minute1:02d}, {self.testValue}, {self.unit}, {self.status}"
