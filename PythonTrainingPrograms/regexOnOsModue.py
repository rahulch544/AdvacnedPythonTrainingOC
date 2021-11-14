import os

print (os.popen("ps -e").read())


# Using system we get only status codes only
print (os.system("whoami"))

print (os.popen("whoami").read())