from flask import *
obj=Flask(__name__)

@obj.route("/mypage/<int:v>")
def f1(v):
	return render_template('result.html',var=v,L=[10,20,30,40])


if __name__ == '__main__':
	obj.run(debug=True)