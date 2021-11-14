from flask import Flask, render_template
app = Flask(__name__)



posts  = [
    {
        'author':'Corey Schager',
        'title':'Blog Post1',
        'content':'First post content'
    },
       {
        'author':'Abcre Schager',
        'title':'Blog Post2',
        'content':'Second post content'
    }
]
# posts = [{'author':'Corey Schager','title':'Blog Post1','content':'First post content'}]
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts = posts)

@app.route('/about')
def about():
    return render_template('about.html', title = 'About Page')

if __name__ == '__main__':
	app.run(debug=True)

    # or 
    # export FLASK_APP=filename.py
    # flask run