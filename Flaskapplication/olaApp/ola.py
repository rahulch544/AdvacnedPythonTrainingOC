from flask import Flask, render_template, request, redirect,jsonify
import json
obj=Flask(__name__)

#task=[{'place':'Place-1','cab':'micro','cost':455.42}]

records=[(101, 'arun', 1000),(102, 'vijay', 2000),(103, 'bibu', 3000),(104, 'leo', 4000)]

@obj.route("/")
def fx():
    temp =records
    # print (json.dumps(temp))
	return jsonify(records)

if __name__ == '__main__':
	obj.run(debug=True)


# import sqlite2
# db = splite3.connect("/Users/rahulch/Downloads/AdvancedPython/Test.db")
# st = db.cursor()
# st.execute("drop Table  emp")
# st.execute("Create Table  emp(eid Number, ename eext, ecost Number)")

# st.execute("insert into emp(eid, ename, ecost) values(1221,'arun','2323')")
# st.execute("insert into emp(eid, ename, ecost) values(123,'arudfdn',23213213)")
# st.execute("insert into emp(eid, ename, ecost) values(1234321,'adfrdfdun',231323)")
# st.execute("insert into emp(eid, ename, ecost) values(1223411,'ardfddfsdvun',234323)")
# cur.execute("SELECT * FROM emp")