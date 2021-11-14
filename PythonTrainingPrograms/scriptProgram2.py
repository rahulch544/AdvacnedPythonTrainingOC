import re
import subprocess
WH =open("scriptProgramOutput.sh","w")
with open("scriptProgram.sh") as FH:
    for var in FH:
        s=re.sub("#.*","",var)
        if re.search("^$",s):
            continue
        else:
            # print(s.strip())
            WH.write(s)
WH.close()
wobj = open("scriptProgramLog.log","w")
subprocess.call(["/bin/bash","scriptProgramOutput.sh"])
subprocess.call(["/bin/bash","scriptProgramOutput.sh"],stdout=wobj)