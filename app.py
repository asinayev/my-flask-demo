from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def main():
	return redirect('/index')

@app.route('/index', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		ticker = request.form
		return redirect("/result", name = ticker)
 	return render_template('index.html')

@app.route('/result')
def result(name):
	return render_template("result.html", ticker = name)


if __name__ == '__main__':
	app.run(port=33507)
