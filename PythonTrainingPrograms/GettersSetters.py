class classname:
    def __init__(self,a):
        self.__a = a
    def fcn1(self):
        print("Get a value :{}".format(self.__a))
        return self.__a
    def fcn2(self,a):
        self.__a = a
        print("Setting a value :{}".format(self.__a))
    # property(getter, setter, optional destructor)    
    v = property(fcn1,fcn2)    

obj = classname('Hi')
obj.fcn1()
obj.fcn2("RAHUL")
print(obj.v)
obj.v='Tank'
print(obj.v)


class Geeks:
     def __init__(self):
          self._age = 0
       
     # function to get value of _age
     def get_age(self):
         print("getter method called")
         return self._age
       
     # function to set value of _age
     def set_age(self, a):
         print("setter method called")
         self._age = a
  
     # function to delete _age attribute
     def del_age(self):
         del self._age
     
     age = property(get_age, set_age, del_age) 
  
mark = Geeks()
  
mark.age = 10
  
print(mark.age)