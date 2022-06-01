from django.db import models
# class Predefine View Classes.
#create model class.
class Job(models.Model):
    jobtitle = models.CharField(max_length=100)
    jobdiscription = models.CharField(max_length=500)

# Create your models here.
