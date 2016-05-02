SRC = src


all: 
	python $(SRC)/flaskwebserver.py 
	
clean:
	@echo "Nothing to do"
