from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Movies

# Create your views here.


class MovieCreateview(CreateView):
    model=Movies
    fields='__all__'
    success_url=reverse_lazy('home_url')
    
    
class MovieDetailview(ListView):
    model=Movies
    
class MovieUpdateview(UpdateView):
    template_name='app1/movies_updateform.html'
    model=Movies
    fields='__all__'
    
    success_url=reverse_lazy('home_url')
    
class MovieDeleteview(DeleteView):
    model=Movies
    success_url=reverse_lazy('home_url')
    
class Movieview(DetailView):
    model=Movies
    