from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Page
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse,reverse_lazy


# Create your views here.
class PageListView(ListView):
    model = Page

class PageDetailView(DetailView):
    model = Page

class PageCreate(CreateView):
    model = Page
    fields = ['title', 'content' ,'order']
    success_url = reverse_lazy('pages:pages')

    
    #def get_success_url(self):
        #return reverse('pages:pages')

