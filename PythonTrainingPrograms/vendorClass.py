class vendor:
    __vname = ''
    __vid = ''
    __vGst = ''
    def __init__(self,vname,vid,vGst):
        self.__vname = vname
        self.__vid = vid
        self.__vGst = vGst
        print("Vendor-{} \t enrollment is done!!".format(self.__vname))
    def billing(self,product,pcost):
        self.__pcost = pcost*0.18
        self.__total = self.__pcost + pcost
        self.__pname = product
        file = open("logVendorDetails.log","a")
        file.write("VendorName-{}\tProductName-{}\tProductPrice-{}\tProductPrice including GST(18%)-{}\n".format(self.__vname,self.__pname,self.__pcost,self.__total)) 
        file.close()