# import cx_Oracle

import sqlite3
dh = sqlite3.connect("Test.db")
st = dh.cursor()
st.execute("drop Table  emp")
st.execute("Create Table  emp(eid Number, ename eext, ecost Number)")

st.execute("insert into emp(eid, ename, ecost) values(1221,'arun','2323')")
st.execute("insert into emp(eid, ename, ecost) values(123,'arudfdn',23213213)")
st.execute("insert into emp(eid, ename, ecost) values(1234321,'adfrdfdun',231323)")
st.execute("insert into emp(eid, ename, ecost) values(1223411,'ardfddfsdvun',234323)")

v1 = 1
v2 = "Raj"
v3 = 232
st.execute("select * from emp")
print(st.fetchall())
print("----------")
st.execute("insert into emp(eid, ename, ecost) values(?,?,?)",(v1,v2,v3))
st.execute("select * from emp")
for var in st:
    print(var)