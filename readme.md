# Darwin Push Port - Python Client

This is a simple example for retrieving the Darwin Push Port data feed in Python. and system requirements for installation.


# Setup
The following steps are required to setup the client on a Mac machine. For other systems like linux swap out the brew installs for `sudo apt-get ` commands.

    brew install python2
	brew install pip
	git clone xxxxxxxxx
	cd xxxxxx
	pip install virtualenv
	virtualenv -p python2 DarwinPythonClient
	source DarwinPythonClient/bin/activate
	pip install stompy.py

## Update the content

Navigate to `app.py` and edit the queue variable to the queue given in registration of the Darwin Feed portal.

# Run the file

	python app.py
