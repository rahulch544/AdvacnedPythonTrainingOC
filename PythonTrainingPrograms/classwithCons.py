class Enrollment:
    Name =''
    Dept =''
    def __init__(self,var1,var2):
        print("Intilization _step")
        self.Name = var1
        self.Dept = var2
    def fcn2(self):
        print ("Name:{}\tWorking Dept:{}".format(self.Name, self.Dept))
    def fcn3(self,var):
        self.Dept = var
        print("Dept:{}\t is updated".format(self.Dept))
obj1 = Enrollment('Rahul','EEE')


