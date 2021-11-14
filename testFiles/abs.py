# import paramiko   
# import threading
# import time
# import sys
# import json


 

# # declare credentials   
# host = 'rchamant.auto.susengdev2phx.oraclevcn.com'   
# username = 'rchamant'   
# password = 'Luhar1201@'  
# # host = 'arudemo-01.auto.susengdev2phx.oraclevcn.com'   
# # username = 'rchamant'   
# # password = 'Luhar1201'  

# class remote_serverCon(threading.Thread):
#     def __init__(self,name):
#         threading.Thread.__init__(self) # calling parent class constructor
#         self.name=name
#     def run(self):
#         print("This is {} thread".format(self.name))
#         # connect to server   
#         client = paramiko.SSHClient()   
#         # add to known hosts
#         # client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#         client.load_system_host_keys()   
#         try:
#             client.connect(hostname=host, username=username, password=password)
#         except:
#             print("[!] Cannot connect to the SSH Server")
#             exit()
#         # client.connect(host, username=username, password=password)
#         # # read the BASH script content from the file
#         # bash_script = open("remote_machine_env.sh").read() 
#         arguments = ''.join(sys.argv[1::])

#         commands = ['setenv PATH "/ade_autofs/ud222_db/GITOOLS_MAIN_LINUX.X64.rdd/LATEST/gitools/src/dupbugs/utl/../../../../python/bin/:$PATH"','/ade_autofs/ud222_db/GITOOLS_MAIN_LINUX.X64.rdd/LATEST/gitools/bin/absfarmctl backport-analysis  --cand '+ arguments+ '30953224' ]
#         # with open("remote_temp.txt", 'r+') as f:
#         #     f.truncate(0)

#         with open("PythonTrainingPrograms/remote_temp2.txt", 'w') as WH:
#             n = len(sys.argv)
#             WH.write("Number of arguments passed are "+str(n)+"\n")
#             WH.write('Input arguments are '+arguments+'\n')
#             resultset=''
#             for command in commands:
#                 stdin, stdout, stderr = client.exec_command(command) 
#                 # process the output   

#                 if stderr.read() == b'':   
#                     for line in stdout.readlines():   
#                         print(line.strip()) # strip the trailing line breaks  
#                         WH.write(line)     
#                         resultset=resultset+line 
#                 else:
#                     WH.write('error',stderr.read().decode())
#                 err = stderr.read().decode()
#                 if err:
#                     WH.write('error '+ str(stderr.read().decode()))
#                 # close the connection  
#             print (json.dumps(resultset))    
#             WH.close()      
        
# remote_serverObj=remote_serverCon("Thread-1")
# remote_serverObj.start()
# print("Exit from main Thread\n")    
import paramiko   
import threading
import time
import sys
import json


 

# declare credentials   
host = 'rchamant.auto.susengdev2phx.oraclevcn.com'   
username = 'rchamant'   
password = 'Luhar1201@'  


class remote_serverCon(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self) # calling parent class constructor
        self.name=name
    def run(self):
        # connect to server   
        client = paramiko.SSHClient()   
        # add to known hosts
        # client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.load_system_host_keys()   
        try:
            client.connect(hostname=host, username=username, password=password)
        except:
            print("[!] Cannot connect to the SSH Server")
            exit()
        arguments = ''.join(sys.argv[1::])

        commands = ['setenv PATH "/ade_autofs/ud222_db/GITOOLS_MAIN_LINUX.X64.rdd/LATEST/gitools/src/dupbugs/utl/../../../../python/bin/:$PATH"','/ade_autofs/ud222_db/GITOOLS_MAIN_LINUX.X64.rdd/LATEST/gitools/bin/absfarmctl backport-analysis  --cand '+ arguments ]
        resultset=''
        for command in commands:
            stdin, stdout, stderr = client.exec_command(command) 
            if stderr.read() == b'':   
                for line in stdout.readlines():   
                    resultset=resultset+line 
            else:
                err = stderr.read().decode() 
        print(json.dumps(resultset))    
        
remote_serverObj=remote_serverCon("Thread-1")
remote_serverObj.start()
remote_serverObj.join()