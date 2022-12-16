import subprocess
import re

WH =open("output.txt","w")
with open("temp.txt", 'r') as FH:
    for line in FH:
        x = re.findall( r"(?<=p)3\d+", line)
        if(len(x) > 0):
            WH.write(", ".join(x));
            WH.write(", ");
        
WH.close()        