##Simple Web Server

A simple web server implementation in order to output system information of the machine upon which it is running

##Requirements

In order to run this application all that will need to be installed is Flask, **Soon this will use Docker in order to self build**

To instal flask use `sudo pip install Flask` or if you would like to use a virtual environment

    sudo pip install virtualenv
    mkdir $VIRTUALENVIRONMENTNAME$
    cd $VIRTUALENVIRONMENTNAME$
    virtualenv venv
    . venv/bin/activate
    pip install Flask

##Running

1. Run `make` or `python src/flaskWebServer.py` to run the server
2. Open your browser and go to the url `localhost:5000` or `127.0.0.1:5000`
3. Navigate using interface provided
