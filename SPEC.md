# Specification & Design


This project implements a simple peer-tutoring application written in Django and
uses a PostgreSQL database. The Django project is called `harvard` and it contains
an app called `search` whose main application is to allow users to search for
tutors. Departments have a logo or image associated with them, these images are
under the `media` directory who is designed to handle and store all media file
for the website. The file `manage.py` is our runner file. We use it to implement
database migrations and to run the application.

Inside `harvard`, we find the logic for the Django project. Importantly, we
have the main settings of the project in `settings.py` and main urls in the project
in `urls.py`. Inside `settings.py` we find the specification about the localhost
database implemented in this project:

			DATABASES = {
			    'default': {
			        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Database flavour
			        'NAME': 'peer_tutoring', # Name of the database
			        'USER': 'postgres', # User connecting to our database
			        'PASSWORD': '', # No password
			        'HOST': 'localhost', '127.0.0.1' for localhost through TCP.
			        'PORT': '', # Default is 8000.
			    }
			}

Inside `urls.py`, we find three main urls:

* /admin: This is the admin Django built in backend
* /search: This is our main url (Search app) that we use in this website
* /courses: This is for the REST API Framework. More on that soon.

Our `search` directory contains all the logic for our main application: searching
for courses. It contains the following files:

* `sigrations/`: contains all our code Migrations
* `static/`: contains CSS code and some images for our website design. This is
separated from the `media` directory because this directory is specifically
for the design of website while `media` is used for additional imaging files.
* `templates/`: contains our bootstrap templates
* `admin.py: allows the admin user to register courses, departments, and Schools
through Django's built-in backend application. You can access the admin panel with
`localhost:8000/admin`
* `apps.py`: contains all our Django apps, only the search app
* `forms.py`: used to handle user login and signup
* `models.py`: contains 3 classes: Course, Department, School. Here goes our logic
for storing information in the database.
* `serializers.py`: similar to models.py, this file handles the serialization of data
* `urls.py`: contains the logic behind our application urls. The root url is
`localhost:8000/search`, `localhost:8000/admin` is our admin url, and finally
`localhost:8000/courses` is the url for the REST API.
* `views.py`: contains our python methods. Rendering templates, use sign up, REST API

### Models.py
---

Models.py contains our DB models. There are basically three modules: Departments, Courses, and Schools.

### Templates
---

This project uses bootstrap templates


Rest API
---

This project also implements a simple REST framework where we serialize courses into a JSON type of file.
This logic is specified in by the `url(r'^courses/', views.CourseList.as_view())` url in urls.py

Demo
----

A demo can be found at harvard-peer-tutoring.herokuapp.com
