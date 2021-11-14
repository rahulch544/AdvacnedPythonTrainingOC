from flask import Flask, render_template, request, redirect,url_for
obj=Flask(__name__)

@obj.route("/")
def f1():
	s="<h2><font color=green>Welcome to flask app</font></h2>"
	return s
@obj.route("/home")
def f2():
	return "<h1><font color=blue>Home Page</font></h1>"

@obj.route("/citynews/<city>")
def f3(city):
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