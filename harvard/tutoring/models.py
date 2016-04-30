from django.db import models

class Course(models.Model):
    
	course_code = models.CharField(max_length=50)
	course_name = models.CharField(max_length=200)
	department = models.CharField(max_length=200)
	school = models.CharField(max_length=200)
	num_tutors = models.IntegerField(default=0)

	def __str__(self):
		return self.course_code

class Department(models.Model):    
	department_name = models.CharField(max_length=200)

	def __str__(self):
		return self.department_name


class School(models.Model):
	school_name = models.CharField(max_length=200)

	def __str__(self):
		return self.school_name
