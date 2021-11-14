# import os

# p1= subprocess.Popen(["ps","-e"],stdout=subprocess.PIPE)
# p2= subprocess.Popen(["grep","bash"],stdin=p1.stdout,stdout=subprocess.PIPE)
# p3= subprocess.Popen(["wc","-l"],stdin=p2.stdout,stdout=subprocess.PIPE)

# result = p3.communicate()

# print (result)
import subprocess
import socket
n=socket.gethostname()
sshProcess = subprocess.Popen(['ssh', 
                               n],
                               stdin=subprocess.PIPE, 
                               stdout = subprocess.PIPE)
# sshProcess.stdin.write(b"dir")
# sshProcess.stdin.write(b"logout\n")
sshProcess.stdin.write("dir")
sshProcess.stdin.write("logout\n")
sshProcess.stdin.close()


for line in sshProcess.stdout:
    if line == "END\n":
        break
    # print(bytes(line),end="")
    print(line)