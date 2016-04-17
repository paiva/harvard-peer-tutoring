from django.db import models

class Course(models.Model):
    course_code = models.CharField(max_length=50)
    course_name = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    school = models.CharField(max_length=200)

class Department(models.Model):
    department_name = models.CharField(max_length=200)
    department_courses = models.IntegerField(default=0)

class School(models.Model):
    school_name = models.CharField(max_length=200)
    school_courses = models.IntegerField(default=0)