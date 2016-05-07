# Harvard Peer tutoring

This project was developed as part of Harvard's CS50 Final Project. This is a website
that allows tutees to search for tutors and for tutors to accept tutees. This project implements
a Django Framework coupled with a PostgreSQL database


Assumes that you have postgresql installed in your computer. If you don't have postgresql set 
up in your machine, you can follow the instructions here https://help.ubuntu.com/community/PostgreSQL

### Setup

Download source code from with `git clone https://github.com/sap789/harvard-peer-tutoring`

Install python virtual environment with `virtualenv -p python3 venv` and activate with 
`source venv/bin/activate` and download dependencies with `pip install -r requirements.pip`

To run the application 

		cd harvard
		python manage.py runserver

Start the local postgres database with ```pg_ctl -D /usr/local/var/postgres -l /usr/local/var/postgres/server.log start```
* Step 6: Run the app locally on port 5000 with ```python run.py```
* Step 7: Open Google Chrome on http://localhost:5000


The application should be running on localhost:8000 


### Seting up database

This project implements a postgres database. 