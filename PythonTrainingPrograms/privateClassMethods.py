class classname:
    Name = ''
    Dept = ''
    __Age  = 0
    def __init__(self,age,dept,name):
        self.__Age = age
        self.Dept = dept
        self.Name = name
        print ("Object created")
    def get_age(self):
        return self.__Age
    def __del__(self):
        print("Object destroyed")
# obj = classname()
obj = classname(12,'EEE','Rahul')
print(obj.Dept)
# print(obj.__Age)
print(obj.get_age())
