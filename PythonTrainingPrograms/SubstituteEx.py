import re

with open("SubstituteEx.txt","r+") as FH:
    for i in range(20):
        FH.write(str(i) + "subnet-eth0-cus01-10.20.20.40-DRA123\n")   
    with open("temp.txt","r+") as TH:
        print("Writing to temp.txt")
        lineCount = 0
        FH = open("SubstituteEx.txt","r+")
        for line in FH:
            if(lineCount<5):
                TH.write(line)
            elif(lineCount>=5 and lineCount <=10):
                line = re.sub("eth0","eth1",line)
                TH.write(line)
            else:
                TH.write(line)
            lineCount += 1
        FH = open("SubstituteEx.txt","r+")    
        for line in open("temp.txt","r+"):
            FH.write(line)

with open("SubstituteEx1.txt") as FH:
    for line in FH.readlines():
        print(line)
        if (re.search("$[\d-,]+^",line)):
            line = line.strip()
            line = re.split("-|,",line)
            sum = reduce(lambda a,b:int(a)+int(b),line[1:])
            print (line[0], sum)
