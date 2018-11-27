from django.shortcuts import render
from django.views.generic import TemplateView
from home.forms import LoginForm
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):

        return render(request, "index.html" , {})
