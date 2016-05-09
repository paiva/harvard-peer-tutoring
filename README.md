# Harvard Peer Tutoring

### What is Harvard Peer Tutoring?
---

Harvard Peer Tutoring was developed as part of Harvard's CS50 Final Project.
It is a proof-of-concept application that allows Harvard students to search for peer tutors
in a simple, fast, and reliable way.

[need screeshot]

### How does it work?
---

Courses are classified under Departments and Schools. You choose courses you need
help with based on the departments they are based on. For instance, tutoring
assistance on **CS50** would be under the **Computer Science** department and both on
"College" and "Extension" schools.

After choosing a department, you can see courses that have tutors available. If
you need assistance in one of this courses, you can click `Request Tutor` to
request a tutor in that class. 

### Specification
---

This project implements a simple peer-tutoring application and uses a postgresql database.
This Django project is called "Harvard" and it contains an app called "search". The directory
`media` contains all the media files, especifically it contains the logos of the course departments
implemented.

In a vary generic level, this app classifies courses by departments. Each departmen, such as Computer Science,
contains courses such as "CS50". For this project, we have implemented a simple proof-of-concept by implementing
only three departments (Computer Science, Statistics, and Economics).

Models.py
----

Models.py contains our DB models. There are basically three modules: Departments, Courses, and Schools.

Templates
----

This project uses bootstrap templates


Rest API
---

This project also implements a simple REST framework where we serialize courses into a JSON type of file.
This logic is specified in by the `url(r'^courses/', views.CourseList.as_view())` url in urls.py

Demo
----

A demo can be found at harvard-peer-tutoring.herokuapp.com

# Setup and Installation

First, install python virtual environment with `virtualenv -p python3 venv` and activate with the virtual
environment with `source venv/bin/activate` and download dependencies with `pip install -r requirements.pip`

To run the application

		cd harvard
		python manage.py runserver

Assumes that you have postgresql installed in your computer. If you don't have postgresql set
up in your machine, you can follow the instructions here https://help.ubuntu.com/community/PostgreSQL


Start the local postgres database with ```pg_ctl -D /usr/local/var/postgres -l /usr/local/var/postgres/server.log start```
* Step 6: Run the app locally on port 5000 with ```python migrate.py runserver```
* Step 7: Open Google Chrome on http://localhost:8000

This project implements a postgres database. Database especification is in setting.py
