SRC = src


all: 
	python $(SRC)/flaskwebserver.py 

simple:	
	python $(SRC)/webserver.py 
	
clean:
	@echo "Nothing to do"
