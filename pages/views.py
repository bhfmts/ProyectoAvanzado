from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Page
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.urls import reverse,reverse_lazy
from .forms import PageForm
from django.shortcuts import redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
class StaffRequiredMixin(object):
    """
    Este mixing requerira'que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin,self).dispatch(request,*args, **kwargs)    

# Create your views here.
class PageListView(ListView):
    model = Page

class PageDetailView(DetailView):
    model = Page

@method_decorator(staff_member_required, name='dispatch')
class PageCreate(CreateView):
    model = Page
    form_class = PageForm
    # nos podemos ahorrar esto porque ya están en el archivo forms.py: fields = ['title', 'content' ,'order']
    success_url = reverse_lazy('pages:pages')
    
@method_decorator(staff_member_required, name='dispatch')
class PageUpdate(UpdateView):
    model = Page
    form_class = PageForm

    template_name_suffix = '_update_form'
    
    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'
    
    #def get_success_url(self):
        #return reverse('pages:pages')
@method_decorator(staff_member_required, name='dispatch')
class PageDelete(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')

