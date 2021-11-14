from abc import ABC, abstractmethod
# from abc import ABCMeta, abstractmethod 

class box(ABC):
    @abstractmethod
    def f1(self):
        pass
    def f2(self):
        print("this is concrete method")


class box1(box):
    def f1(self):
        pass
    def f2(self):
        print("Box1 f2 Block")

class box2(box):

    def f1(self):
        pass        
    def f2(self):
        super().f2()

class box3(box):
     def f1(self):
        pass       

obj1 = box1()
obj2 = box2()
obj1.f1()
obj1.f2()

obj2.f1()
obj2.f2()        