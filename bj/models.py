from django.db import models
import json
import datetime
import ast
from django.utils import timezone
# Create your models here.
class Company(models.Model):
	comany_name = models.CharField(max_length=70)
	year_founded = models.IntegerField()
	no_of_employee = models.TextField(max_length=80)
	about  = models.CharField(max_length=900)

class Role(models.Model):
	role = models.CharField(max_length=70)
	about = models.CharField(max_length=500)

class Job_english(models.Model):
	role_id  = models.ForeignKey(Role)
	company_id = models.ForeignKey(Company)
	comany_name = models.CharField(max_length=70)
	job_role = models.CharField(max_length=100)
	in_hand_salary = models.IntegerField()
	location = models.CharField(max_length=70)
	i = models.CharField(max_length=70)
	salary_detail = models.CharField(max_length=90)
	job_type = models.CharField(max_length=70)
	shift = models.CharField(max_length=70)
	timings = models.CharField(max_length=70)
	education_requried = models.CharField(max_length=70)
	min_work_exp = models.CharField(max_length=70)
	job_description = models.CharField(max_length=500)
	accomodation = models.CharField(max_length=70)
	food = models.CharField(max_length=70)

class Job_hindi(models.Model):
	role_id  = models.ForeignKey(Role)
	company_id = models.ForeignKey(Company)
	comany_name = models.CharField(max_length=70)
	job_role = models.CharField(max_length=100)
	in_hand_salary = models.IntegerField()
	location = models.CharField(max_length=70)
	i = models.CharField(max_length=70)
	salary_detail = models.CharField(max_length=90)
	job_type = models.CharField(max_length=70)
	shift = models.CharField(max_length=70)
	timings = models.CharField(max_length=70)
	education_requried = models.CharField(max_length=70)
	min_work_exp = models.CharField(max_length=70)
	job_description = models.CharField(max_length=500)
	accomodation = models.CharField(max_length=70)
	food = models.CharField(max_length=70)

class Job_hinglish(models.Model):
	role_id  = models.ForeignKey(Role)
	company_id = models.ForeignKey(Company)
	comany_name = models.CharField(max_length=70)
	job_role = models.CharField(max_length=100)
	in_hand_salary = models.IntegerField()
	location = models.CharField(max_length=70)
	i = models.CharField(max_length=70)
	salary_detail = models.IntegerField()
	job_type = models.CharField(max_length=70)
	shift = models.CharField(max_length=70)
	timings = models.CharField(max_length=70)
	education_requried = models.CharField(max_length=70)
	min_work_exp = models.CharField(max_length=70)
	job_description = models.CharField(max_length=500)
	accomodation = models.CharField(max_length=70)
	food = models.CharField(max_length=70)



