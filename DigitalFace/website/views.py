from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic.edit import CreateView
from django.views.generic import FormView
from .forms import Userform
from django.urls import reverse
from .models import temp,Person

class PersonCreate(CreateView):
    model=Person
    template_name = 'website/registration.html'
    fields = ['Name', 'DOB','Street','Locality', 'City', 'District', 'State', 'Pincode','UID']
    def get_absolute_url(self):
        return reverse('/')

#class tempcreate(CreateView):


# Create your views here.
def index(request):
    return HttpResponse("Hello world")



