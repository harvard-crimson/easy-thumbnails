Testing
=======

1. Install tox (``pip install tox``)
2. Run ``tox``

If you want to test against previous versions of Python then you might need to
install them, too. Here's a quick log for installing them in Ubuntu (probably
just as relevant for Debian)::

	sudo add-apt-repository ppa:fkrull/deadsnakes
	suda apt-get update
	sudo apt-get install python2.5 python2.5-dev python2.6 python2.6-dev

	sudo apt-get install build-essential python-dev python3-dev 
	sudo apt-get install libsqlite3-dev libjpeg8-dev zlib1g-dev
