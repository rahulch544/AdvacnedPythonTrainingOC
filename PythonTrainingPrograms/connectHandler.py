class connectHandler:
    def __init__(self,**a):
        print(a)
        self.a = a
        self.a['K'] = 'updated'
        for var in self.a:
            pass
    def method1(self):
        return self.a

    def __enter__(self): 
        return self

    def __exit__(self,*a):
        print("Exit block")

           
d = {"port":80,"server":'apache2',"file":'/usr/lib/bin/cgi-bin'}
obj = connectHandler(**d)
obj.method1()             

with connectHandler(**d) as obj1:
    print(obj1.a)