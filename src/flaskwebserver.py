from flask import Flask, redirect, url_for, render_template
import subprocess
import os

app = Flask(__name__)

@app.route("/stats")
def stats():
	sInfo = getUsageInfo()
	
	CPU = "50%"
	MEM = "60%"
	l = ["l1","l2","l3","l4","l5","Other"]
	d = [12,15,17,20,19,100-12-15-17-20-19]
	return render_template("main.html",CPU=CPU,MEM=MEM,l=l,d=d)

@app.route("/")
def index():
	return redirect(url_for('stats'))

@app.route("/servInfo")
def servInfo():
	sInfo = getUsageInfo()
	return render_template("servInfo.html", sInfo = sInfo)

def getUsageInfo():
	myenv = os.environ.copy()
	myenv["COLUMNS"] = "512"
	return subprocess.check_output(["top","-b", "-n", "1"], env=myenv)

if __name__ == "__main__":
	app.debug=True
	app.run()
