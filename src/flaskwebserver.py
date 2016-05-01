from flask import Flask, redirect, url_for
import subprocess
import os

app = Flask(__name__)

@app.route("/stats")
def stats():
	myenv = os.environ.copy()
	myenv["COLUMNS"] = "512"
	s = subprocess.check_output(["top","-b", "-n", "1"], env=myenv)
	return str(s)

@app.route("/")
def index():
	return redirect(url_for('stats'))


if __name__ == "__main__":
	app.debug=True
	app.run()
