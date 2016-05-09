# Harvard Peer Tutoring

### What is Harvard Peer Tutoring?
---

Harvard Peer Tutoring was developed as part of Harvard's CS50 Final Project.
It is a proof-of-concept application that allows Harvard students to search for peer tutors
based on the departments (or concentrations) in a simple, fast, and reliable way.

[need screeshot]

For this delivery, we have only implemented 13 courses in three departments:

* Computer Science
* Statistics
* Economics

And, two schools:

* College
* Extension

### How does it work?
---

Courses are classified under Departments and Schools. You choose courses you need
help with based on the departments they are based on. For instance, tutoring
assistance on **CS50** would be under the **Computer Science** department and both on
"College" and "Extension" schools.

After choosing a department, you can see courses that have tutors available. If
you need assistance in one of this courses, you can click `Request Tutor` to
request a tutor in that class.

# Setup and Installation

First, install python virtual environment with `virtualenv -p python3 venv` and
activate with the virtual environment with `source venv/bin/activate` and download
dependencies with `pip install -r requirements.pip`

To run the application

		cd harvard
		python manage.py runserver

Assumes that you have postgresql installed in your computer. If you don't have postgresql set
up in your machine, you can follow the instructions here https://help.ubuntu.com/community/PostgreSQL


Start the local postgres database with ```pg_ctl -D /usr/local/var/postgres -l /usr/local/var/postgres/server.log start```
* Step 6: Run the app locally on port 5000 with ```python migrate.py runserver```
* Step 7: Open Google Chrome on http://localhost:8000
