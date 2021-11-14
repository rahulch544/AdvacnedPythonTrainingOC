# # Pretty print interpeter
# import pprint 
# #list of list, tuple ,dict
# L=[]
# L.append(100)
# L.append(245.52)
# L.append('data')
# print L, type(L)

# l=[]
# l.append(['a','b','c'])
# l.append((100,200,400))
# l.append({'a':'v','b':'c','c':3})

# print l, type(l)


# # dict inside dict 
# d = {'a':{'a':1,'b':2},'b':'b'}

# print d['a']['a']
# print d
# pprint.pprint(d)

# # JSON ARRAY --> PYTHON LIST
# # JOSN OBJECT --> PYTHON OBJECT


# def fcn():
#     a =100;

# print fcn()==None

# try:
#     dict_ = {} 
#     fileContent = open("property.txt")
#     for line in fileContent:
#         sp = line.split('=')
#         dict_[sp[0]]= sp[1].strip('\n')
#     pprint.pprint(dict_)
#     dict_['onboot']='Yes'
#     dict_['bootstrub']='static'
#     dict_['IP']='10.20.30.40'
#     dict_['prefix']=24
# finally:
#     # pprint.pprint(dict_)
#     for var in dict_:
#         print ("{}\t{}".format(var,dict_[var]))
#     print "Reached final block"
#     # creates new file and appends text in it or 
#     # truncates file content and adds new content
#     with open("newproperty.txt","w") as WH:
#         for var in dict_:
#             WH.write("{}={}\n".format(var,dict_[var]))

# #  dictionary.get('key') ==> works even if key is not present by returning None value
# #  dictionary['key'] ==> throws key error if key is not present

# i = 0
# lis = []
# while i<5:
#     val = input("Enter your Emp Name: ")
#     val = val.title()
#     lis.append(val)
#     i+=1
# else:
#     print "Size of list:{}".format(len(lis))

# for var in lis:
#     print var

# # write a python program
# # step 1: create an empty dict 
# # step 2: use forloop + range() - 5times
# # step 3:    -> read a alias name from <STDIN>(ex: host01) //key
# # step 4:    -> read a Ipaddress from <STDIN> (ex: 10.20.30.40) //value
# # step 5:   --> add input data to existing dict 
# #               Note: alias name must be unique  - use membership operator 
# # step 6: display key/value

# systems ={}
# for i in range(5):
#     nameOfHost = input("Please enter host name ").title()
#     ipAddress = input("Please enter IP address ").strip()
#     if(systems.get(nameOfHost)!=None):
#         print ("Host is alread exist")
#         i-=1
#         continue;
#     systems[nameOfHost] = ipAddress
# for a in systems.keys():
#     print ("HostName:{}\t IP address:{}".format(a,systems[a]))


# # Functions::
# # 1. Require argument functions eg: fcn(a), can be called : fcn(value)
# # 2. Default argument functions eg: fcn(b='value'), can be called : fcn(val) or fcn()
# # 3. tuple arguments functions eg : fcn(*a) , can be called : fcn() or fcn(val1) or fcn(val1,val2,...)
# # 4. keyword arguments functions eg: fcn(**a), can be called : fcn() or fcn(key1=val1,...)
# # ******Order*******
# # function( Required args, defaultArguments, tupleArguments, keywordArguments)


# def voidfcn():
#     a =10.20.30.40
#     #do the rest of operations
#     #by default following will be added internally
#     return None
# def returnFcn():
#     # Do operations
#     return value
#     #internally added
#     return None

# def aruguments(a,b,v):
#     # DO operations
#     return None
# def defaultArguments(a,b=0):
#     #do operations
#     #internally added
#     return None

# # any  number of arugements (always aruguments are stored in tuple format only args len 0 or more)
# def anyNoOfArgs(*tupleVarName):
#     print(type(tupleVarName),len(tupleVarName))
#     print(tupleVarName)
#     #internally added
#     return None

# # Complex function

# def complexFunction(a,b,c,d=1,e,f=6,*g):
#     #do operations
#     #internally added
#     return None


# # function with keyword argument

# def dictFunction(**args):


# dictFunction(hi='hi')
# dictFunction(dictVarName);


from functools import reduce

var = filter(lambda a: 'sales' in a, [line.strip() for line in open("temp.csv").readlines()])
print (var)

print ("****")
tmp = reduce(lambda a,b:int(a)+int(b),map(lambda a:a.split(",")[-1],var))
print (tmp)
var = reduce(lambda a,b: int(a.split(",")[-1])+int(b.split(",")[-1]),filter(lambda a: 'sales' in a, [line.strip() for line in open("temp.csv").readlines()]))

print(var)

# reduce(lambda a,b:int(a)+int(b),map(lambda a:a.split(",")[-1],filter(lambda a:'sales' in a,map(lambda a:a,open("D:\\emp.csv").readlines()))))