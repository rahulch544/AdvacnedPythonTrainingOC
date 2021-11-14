class Enrollment:
    Name =''
    Dept =''
    def fcn1(self,var1,var2):
        print("Intilization _step")
        self.Name = var1
        self.Dept = var2
    def fcn2(self):
        print ("Name:{}\tWorking Dept:{}".format(self.Name, self.Dept))
    def fcn3(self,var):
        self.Dept = var
        print("Dept:{}\t is updated".format(self.Dept))
obj1 = Enrollment()
obj1.fcn1()


                