from flask import Flask, render_template, request, redirect, url_for
from makeplot import makeplot	

app = Flask(__name__)

@app.route('/')
def main():
	return redirect('/index')

@app.route('/index', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		ticker = request.form['ticker']
		makeplot(ticker)
		return render_template("lines.html")
 	return render_template('index.html')


if __name__ == '__main__':
	app.run()
