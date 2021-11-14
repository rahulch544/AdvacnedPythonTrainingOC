import re
import subprocess
import os
# WH =open("process_cpct_defintions.sh","w")
# with open("/Users/rahulch/Downloads/arusprint01/JenkinsJobFiles/process_bugdb_release_bugs.sh") as FH:
#     for var in FH:
#         s = re.sub('DatabaseConfig.cfg','Users/rahulch/Downloads/arusprint01/JenkinsJobFiles/DatabaseConfig.cfg',var)
#         s = re.sub("bugdb_release","cpct_definitions",s)

#         WH.write(s)

# WH.close()
# os.system("cp process_cpct_defintions.sh /Users/rahulch/Downloads/arusprint01/JenkinsJobFiles/")
wobj = open("process_cpct_defintions.log","w")
subprocess.call(["/bin/bash","process_cpct_defintions.sh"],stdout=wobj)
