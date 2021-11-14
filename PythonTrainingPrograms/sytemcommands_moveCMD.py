import subprocess
import re

# lis = subprocess.run(["ls","/Users/rahulch/Downloads"])
# lis = subprocess.Popen(["ls","/Users/rahulch/Downloads"])
wobj = open("filesInDir.log","r+")
# subprocess.call(["ls","/Users/rahulch/Downloads"])
lis = subprocess.call(["ls","/Users/rahulch/Desktop"],stdout=wobj)

print(lis,"print lis object")

with open("filesInDir.log", 'r') as WH:
    for i in WH:
       if (re.search("^payment",i)):
           print("File Name ",i)
           SrcfolderPath = "/Users/rahulch/Desktop/"
        #    subprocess.call('mkdir '+ SrcfolderPath+"paymentsLL",shell=True)
           DestfolderPath = "/Users/rahulch/Downloads/paymentsLL/"
           command = 'mv ' +'"'+SrcfolderPath+i.strip()+'"'+' "'+DestfolderPath+'"'
           print (command)
           subprocess.call(command,shell=True)

