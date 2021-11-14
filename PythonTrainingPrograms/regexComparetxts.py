import subprocess
import re

fromui =[]

with open("PythonTrainingPrograms/nondelta.log", 'r') as WH:
    for line in WH:
       if (re.search("Processed$",line)):
           lis = re.findall(r"\d{7,8}",line)
           if(len(lis)>0):
            fromui.append(int(lis[0]))
# print (res)     
fromui =set(fromui)      
print(len(fromui))
with open("PythonTrainingPrograms/nondelta.txt", 'w') as WH:
    WH.write(str(fromui))

backend =[]
with open("PythonTrainingPrograms/nondelta2.txt", 'r') as WH:
    for line in WH:
        backend = list(map(lambda x:int(x), line.strip().split(',')))
backend = set(backend)      
print(len(backend))

print (backend.difference(fromui))

# {31421316, 31595025, 29378834, 33332891, 31794336, 32619298, 32267171, 30886188, 
# 30765486, 32492343, 33388473, 32522300, 33060161, 32941509, 32441671, 32186186, 
# 33218518, 33109335, 32245850, 32089820, 32387555, 33127141, 32996071, 32902635,
#  30729839, 32654962, 32874995, 32044533, 32489206, 32127227, 32739966}