import re
# print(help(re.sub))

# re.sub("olfpattern(Regx)","RepacledString","InputString") ->String
# re.subn("olfpattern(Regx)","RepacledString","InputString") ->tuple (ChangedString, NoOfRepalcements)

print ( re.sub('bash','ksh','1010:pts/1:bash'))
print ( re.subn('bash','ksh','1010:pts/1:bsh'))

# print(help(re.findall()))

#  Enumerate 

# for  var in enumerate(open(file),startIndex=0):
#     output will be var = (index, line at index)

n = input("Enter any two digits: ")
import re

if re.search("^\d{1,2}$",n):
    print ("Valid")
else:
    print("Invalid")
    