import re
with open("regexSplitex.txt","r") as FH:
    for line in FH:
        detail = re.split("[^\w]",line.strip())
        print("Name {}\t Price {}".format(detail[1], detail[-1]))