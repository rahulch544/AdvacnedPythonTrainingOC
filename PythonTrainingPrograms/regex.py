import re

# Automatically file will be closed by this nblock
# with open("regexFile.txt","r") as FH:
#         for var in FH:
#             if(re.search("sales",var)):
#                 # print(var.strip())
#                 pass
print (re.findall("bash","bas:x:bash:usr:bin:bash:root:bash"))
print (re.search("bash","bas:x:bash:usr:bin:bash:root:bash"))

#Special Characters

# +  one or more times repeated previous characters

s = 'i am from Asiaaaa'

print (re.search('ia+',s))


# #search
# re.search()
# re.findall()

# #substitution
# re.sub()
# re.subn()

# #Split
# re.split()

searchString = "rptno="
i = 0
with open("PythonTrainingPrograms/bugfixList.txt","r") as RO:
    with open("PythonTrainingPrograms/bugfixList","w") as WO:
        for line in RO:
            # print(line)
            if(re.search(searchString,line)):
                if(i%2==0):
                    WO.write("CI BUG "+ line)
                else:    
                     WO.write("Base Bug BUG "+ line)
                i+=1     


