from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def login_page(request):
    template = loader.get_template('simplistApp/login_page.html')
    return HttpResponse(template.render(request))