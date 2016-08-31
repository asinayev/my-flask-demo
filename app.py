from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def main():
	return redirect('/index')

@app.route('/index', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		return redirect("result.html")
 	return render_template('index.html')

 @app.route('/result', methods=['GET', 'POST'])
def result():
	if request.method == 'POST':
		ticker = request.form
		return render_template("result.html", result = ticker)


if __name__ == '__main__':
	app.run(port=33507)
