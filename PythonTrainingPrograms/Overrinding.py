class A:
    def fx(self):
        print('Fx block from class A')
    def fz(self):
        print('Fz block from class A')
class B(A):
    def fx(self):
        print("fx block from class B")
        #in order to call parent ,method
        A.fx(self)
        # or if method name is same only latest version only
        # super(B,self).fx()
obj = B()
obj.fx()

# check whether istance is of object & class

if(isinstance(obj,B)):
    print('obj is instance of B class')
if(isinstance(obj,A)):
    print('obj is instance of A class')    

# check whether B is child of parent class A

if(issubclass(B,A)):
    print('B is sub class of A')