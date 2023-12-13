# from django.shortcuts import render, HttpResponse

from django.contrib.auth.mixins import LoginRequiredMixin 
from django.views import generic

# Create your views here.

#def home(request):
#    return render (request, 'home.html')

class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'home.html'
    login_url = 'login'
