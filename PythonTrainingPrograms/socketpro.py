import subprocess
import socket
import getpass
n=socket.gethostname()
p=getpass.getpass('Enter a password:')
sshProcess = subprocess.Popen(['ssh',n,p],stdin=subprocess.PIPE,stdout = subprocess.PIPE)
sshProcess.stdin.write("dir")

sshProcess.stdin.write("logout\n")
sshProcess.stdin.close()


for line in sshProcess.stdout:
    if line == "END\n":
        break
    print((line))