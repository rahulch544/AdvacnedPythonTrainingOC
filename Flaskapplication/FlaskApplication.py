from flask import Flask, render_template, request, redirect
from bs4 import BeautifulSoup


# print(soup.prettify())

app = Flask(__name__)

obj=Flask(__name__)

@obj.route("/enroll")
def enrollPage():
	return render_template('enroll.html')

@obj.route("/home")
def home():
	return "<h1><font color=blue>Home Page</font></h1>"

@obj.route("/seedData")
def seedData():
	return "<h2>About {} news page.".format(city)

@obj.route("/contact/<pin>")
def f4(pin):
    if pin =="state1":
        return redirect("/state1")
    else:
        return redirect(url_for('f5'))

@obj.route("/state1")
def f5():
    return "<h2>pin number is 122323</h2>"


if __name__ == '__main__':
	obj.run(debug=True)