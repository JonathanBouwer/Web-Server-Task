from flask import Flask, redirect, url_for, render_template
import subprocess
import os

app = Flask(__name__)

@app.route("/stats")
def stats():
	myenv = os.environ.copy()
	myenv["COLUMNS"] = "512"
	topData = subprocess.check_output(["top","-b", "-n", "1"], env=myenv)
	sInfo = topData
	return render_template("main.html", sInfo = sInfo)

@app.route("/")
def index():
	return redirect(url_for('stats'))


if __name__ == "__main__":
	app.debug=True
	app.run()
