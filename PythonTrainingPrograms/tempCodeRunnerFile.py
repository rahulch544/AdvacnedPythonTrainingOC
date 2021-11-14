class filesys:
    def __init__(self,fname,mode="r"):
        self.fname=fname
        self.mode=mode
        self.fp=''
    def __enter__(self):
        self.fp=open(self.fname,self.mode)
        return self.fp
    def __exit__(self,*exc):
        self.fp.close()
        
with filesys('p1.log','w') as fobj:
    fobj.write("data-1\n")
    for var in range(2,6):
        fobj.write("data-"+str(var)+"\n")