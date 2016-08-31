from flask import Flask, render_template, request, redirect, url_for	

app = Flask(__name__)

@app.route('/')
def main():
	return redirect('/index')

@app.route('/index', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		tickerdict = request.form
		return render_template("result.html", ticker = tickerdict['ticker'])
 	return render_template('index.html')


if __name__ == '__main__':
	app.run()
