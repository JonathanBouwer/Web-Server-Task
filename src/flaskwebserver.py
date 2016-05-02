from flask import Flask, redirect, url_for, render_template
import subprocess
import os
import re

app = Flask(__name__)

@app.route("/stats")
def stats():
	sInfo = getUsageInfo()
	#TODO Actually populate data
	m = re.search('Mem:(.*)(\\d*)(.*)total,(.*)(\\d*)(.*)used',sInfo)
	memUse = float(int(m.group(4).strip())/float(m.group(1).strip())*100)
	cur = ""
	pastPID = False
	cpuUse = 0
	l = ["","","","","","Other","Free"]
	d = [0,0,0,0,0,0,0]
	
	for c in sInfo:
		if c== "\n":
			if pastPID:
				line = cur.split()
				cpuUse+=float(line[8])
				thisMemUse = float(line[9])
				for i in range(0,5):
					if(thisMemUse>d[i]):
						for j in range(4,i,-1):
							d[j] = d[j-1]
							l[j] = l[j-1]
						d[i] = thisMemUse
						l[i] = line[1]+":"+line[11]
						break
			if "PID" in cur:
				pastPID = True
			cur = ""
		else:
			cur=cur+c
			
	d[5] = memUse
	d[6] = 100-memUse
	for i in range(0,5):
		d[5]-=d[i]
	for i in range(0,7):
		d[i]=round(d[i],2)
	CPU = "%.3f"%cpuUse+"%"
	if cpuUse>100:
		CPU = CPU+" (This value shows the CPU usage in relation to the power of 1 core; i.e there is more than 1 core is being used)"
	MEM = "%.3f"%memUse+"%"
	
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
