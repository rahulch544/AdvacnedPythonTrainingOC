import re
import os

s="root:x:bin,bash:usr"

#split splits on single char only
print (s.split(":|,"))

print (re.split(":|,",s))

print ( os.popen("ps").read())
