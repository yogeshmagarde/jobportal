from django.shortcuts import render
from . models import Job
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView


class JobCreate(CreateView):
    model = Job
    fields = ['jobtitle','jobdiscription']
    def get_success_url(self):
        return reverse('login')

class Joblist(ListView):
    model = Job     # Job.objects.all()   
    fields = ['jobtitle','jobdiscription']

class JobDetailView(DetailView):
  model = Job   # Job.objects.all() 


class JobUpdate(UpdateView):

  model = Job      # Job.objects.all()

  fields = ['jobtitle', 'jobdiscription']

  success_url = '/class/joblist'

class JobDelete(DeleteView):

  model = Job    # Job.objects.all()
  success_url = '/class/joblist'
  
    
# Create your views here.
