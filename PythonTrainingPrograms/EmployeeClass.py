#   ---in python latest versions
from abc import ABC, abstractmethod 
 
# from abc import ABCMeta, abstractmethod 



class Employee(ABC):
    # __metaclass__ = ABCMeta  
    def __init__(self,name=""):
        self.emp_name = name
    @property
    def ename(self):
        return self.emp_name
    @abstractmethod
    def getSalary(self):
        pass


class FulltimeEmp(Employee):
    def __init__(self,name,salary):
        super().__init__(name) #Calling parent constructor
        self.salary = salary
    def getSalary(self):
        return self.salary    

class HourlyEmp(Employee):        
    def __init__(self,name,hrs,rate):
        super().__init__(name) #Calling parent constructor
        self.hrs = hrs 
        self.rate = rate

    def getSalary(self):
        return self.hrs * self.rate    

# FulltimeEmpObj = FulltimeEmp("Ram",24000)
# HourlyEmpObj = HourlyEmp("Lakshman",30,30)


class payroll:
    def __init__(self):
        self.empList = []
    def enroll(self,a):
        self.empList.append(a)
    def display(self):
        for var in self.empList:
            print ("Employee Name {}\t Salary {}".format(var.ename,var.getSalary()))

payrollObj = payroll()
# payrollObj.enroll(FulltimeEmp("Ram",24000))
payrollObj.enroll(HourlyEmp("Lakshman",30,30)) 

payrollObj.display()