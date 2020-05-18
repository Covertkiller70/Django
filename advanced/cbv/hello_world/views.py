from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, ListView, CreateView, UpdateView, DeleteView
from hello_world import models

# Create your views here.
class IndexView(TemplateView):
    template_name = 'hello_world/index.html'

class SchoolListView(ListView):
    context_object_name = 'schools'
    template_name = 'hello_world/school_list.html'
    model = models.School

class SchoolDetailView(DetailView):
    template_name = 'hello_world/school_data.html'
    model = models.School

class SchoolCreateView(CreateView):
    model = models.School
    fields = ('name','principal','location')

class SchoolUpdateView(UpdateView):
    fields = ['name','principal']
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy('hello_world:list') 