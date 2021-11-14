import os

#os.mkdir os.rmdir os.listdir() os.chdir() os.walk()
# os.path.isfile() os.path.isdir() os.path.exists() ---> True/False <== Validation

print (os.popen("sh shellscript.sh").read())