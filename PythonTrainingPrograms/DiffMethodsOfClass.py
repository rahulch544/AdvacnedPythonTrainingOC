class classname:
    def objmethod(self):
        print("Instance method only")
    @classmethod
    def decoratorClassMethod(cls):
        print("Class Method")
    @staticmethod
    def saticMethod():
        print("This is static method")

obj= classname()

# calling from object
obj.objmethod()
#not preferred way, it is quivalent class.methodname
obj.decoratorClassMethod()
obj.saticMethod()

classname.decoratorClassMethod()
classname.saticMethod()