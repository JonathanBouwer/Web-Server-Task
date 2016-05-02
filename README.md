#Simple Web Server

A simple web server implementation in order to output system information of the machine upon which it is running

#Requirements

In order to run this application all that will need to be installed is Python and Flask

#Installation and Running

##Manual

###Installation

To install flask use `sudo pip install Flask` or if you would like to use a virtual environment run the commands

    sudo pip install virtualenv
    mkdir $VIRTUALENVIRONMENTNAME$
    cd $VIRTUALENVIRONMENTNAME$
    virtualenv venv
    . venv/bin/activate
    pip install Flask
    
###Running

1. Run `make` or `python src/flaskWebServer.py` to run the server
2. Open your browser and go to the url `localhost:5000` or `127.0.0.1:5000`
3. Navigate using interface provided

##Docker

###Installation

Simply run `docker build -t simplewebserver .`, this will need some time to download a few dependancies

###Running

1. Run `docker run -d -p 5000:5000 simplewebserver`
2. Open your browser and go to the url `localhost:5000` or `127.0.0.1:5000`
3. Navigate using interface provided

*Running in docker will only show usage information of that specific docker container, not the entire machines usage in order to maintain docker container independance
