import subprocess
import re

wobj = open("/Users/rahulch/Downloads/AdvancedPython/filesInDir.log","r+")
# subprocess.call(["ls","/Users/rahulch/Downloads"])
lis = subprocess.run("find /Users/rahulch/Downloads/AdvancedPython/ -maxdepth 1 -type f".split(" "),stdout=wobj)

# print(lis,"print lis object")

with open("filesInDir.log", 'r') as WH:
    for i in WH:
       if (True or re.search(".*",i)):
        #    print("File Name ",i)
           SrcfolderPath = ''
        #    subprocess.call('mkdir '+ SrcfolderPath+"paymentsLL",shell=True)
           DestfolderPath = "/Users/rahulch/Downloads/AdvancedPython/PythonTrainingPrograms/"
           command = 'mv ' +'"'+SrcfolderPath+i.strip()+'"'+' "'+DestfolderPath+'"'
           print (command)
           subprocess.call(command,shell=True)