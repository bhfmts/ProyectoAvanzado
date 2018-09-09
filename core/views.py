from django.shortcuts import render
from django.views.generic.base import TemplateView

class HomePageView(TemplateView):    
    template_name = "core/home.html"
    def get(self, request, *args, **kwards):
        return render(request, self.template_name, {'title':"Mi super web"})


class SamplePageView(TemplateView):
    template_name = "core/sample.html"
