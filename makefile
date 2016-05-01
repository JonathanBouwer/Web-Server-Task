SRC = src


all: 
	python $(SRC)/webserver.py 

flask:
	python $(SRC)/flaskwebserver.py 
	
clean:
	@echo "Nothing to do"
