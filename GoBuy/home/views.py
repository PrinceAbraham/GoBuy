from django.shortcuts import render
from django.views.generic import TemplateView
from home.forms import LoginForm
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = LoginForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                #admin panel or products
                return HttpResponseRedirect('/thanks/')
        else:
            form = LoginForm()

        return render(request, "index.html" , {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
        args = { 'form': form, 'username': username, 'password': password}
        return render(request,  "add.html" , args)
