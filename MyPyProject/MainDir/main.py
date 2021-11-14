#!/usr/bin/env python3


# Flask is a popular Python web framework, meaning it is a third-party Python library used for developing web applications.
#
# jsonify is a function in Flask's flask. json module. 
# jsonify serializes data to JavaScript Object Notation (JSON) format,
#  wraps it in a Response object with the application/json mimetype. 
#  Note that jsonify is sometimes imported directly from the flask module instead of from flask.

#  render_template is used to generate output from a template file 
# based on the Jinja2 engine that is found in the application's templates folder

# redirect URL redirection, also known as URL forwarding, 
# is a technique to give more than one URL address to a page, a form, or a whole Web site/application. 

from flask import Flask, render_template, request, redirect,jsonify,url_for

# The requests module allows you to send HTTP requests using Python. 
# The HTTP request returns a Response Object with all the response data (content, encoding, status, etc).
import requests

# Beautiful Soup is a Python library for pulling data out of HTML and 
# XML files. It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree
from bs4 import BeautifulSoup

# Creating Flask object using thread name as input
app = Flask('__main__')

@app.route('/')
@app.route('/home')
def home():
#    return """<h1><font color=cyan>Home Page</font>
#             <sub style='font-size:30%'>RCHAMANT</sub></h1>"""
    return render_template('home.html')

def privatehome(name):
#    return """<h1><font color=cyan>Home Page</font>
#             <sub style='font-size:30%'>RCHAMANT</sub></h1>"""
    return """<h1><font color=cyan>Home Page</font>
            <sub style='font-size:30%'>%name</sub></h1>"""+name
app.add_url_rule('/privatehome/<name>','privatehome',privatehome)    

@app.route('/admin')  
def admin():  
    return 'admin'  

# Dynamic routing example, it uses function name as input string parameter and using URL parameters
@app.route('/user/<name>')  
def user(name):  
    if name == 'admin':  
        return redirect(url_for('admin')) 

# getting arguments from request using request.form.
@app.route('/login',methods = ['POST'])  
def login():  
      uname=request.form['uname']  
      passwrd=request.form['pass']  
      if uname=="ayush" and passwrd=="google":  
          return "Welcome %s" %uname

# Running application only if we running this file
if __name__ == '__main__':
    # app.run(host, port, debug, options)  
    app.run(port=1312,debug=True)
