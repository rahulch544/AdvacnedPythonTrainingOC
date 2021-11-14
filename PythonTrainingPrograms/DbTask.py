import sqlite3

def DbClass():
    class dbTransaction:
        def __init__(self):
            self.db = sqlite3.connect("DbTask.db")
        def __enter__(self):
            self.cursor = self.db.cursor()
            return self.cursor
        def __exit__(self, *args):
            print("Closing DB connection")
            self.db.close()
    dbCursorObj =  dbTransaction()
    return dbCursorObj             

with DbClass() as st:
    try:
        st.execute("drop Table  emp")
    finally:
        pass
    st.execute("Create Table  emp(eid Number, ename eext, ecost text)")
    with open("DbInputfie.txt","w") as Ip:
        for var in range(10):
            var =str(var)
            Ip.write(var+",Ram"+var+","+"text"+var+"number"+var+"\n")
    with open("DbInputfie.txt","r") as Ip:
        for var in Ip.readlines():
            #  line = re.split(",",var.strip())
            line = "insert into emp(eid,ename,ecost) values ("+str(var.strip())+")"
            st.execute(line)
            print line
