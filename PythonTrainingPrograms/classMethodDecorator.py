class Enrollment:
    __Name=""
    __Dept=""
    def fcn1(self,Name,Dept):
        self.__Name = Name
        self.__Dept = Dept
    def fcn2(self):
        print("Name:{}\t Working Dept:{}".format(self.__Name,self.__Dept))
    def fcn3(self,Dept):
        slef.__Dept =Dept
    @classmethod
    def fcn4(cls):
        cls.__Place="DefautPlace"
        cls.__Bgroup="DefaultBgroup"
        print (cls)
    def fcn5(self,Place,Bgroup):
        self.__Place = Place
        self.__Bgroup = Bgroup
    def fcn6(self):
        return self.__Name,self.__Place,self.__Bgroup,self.__Dept
   # @classmethod    
    def fcn7(self,Place,Bgroup):
        self.__Place=Place
        self.__Bgroup=Bgroup



obj = Enrollment()
obj.fcn1('rahul','EEE')
# obj.fcn6()
print (dir(Enrollment))
obj.fcn4()
obj.fcn7("Hyd","O+")
print (dir(Enrollment))
print(obj.fcn6())
obj2 = Enrollment()

obj2.fcn1('cham','EEE')
print(obj2.fcn6())