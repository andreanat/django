from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

def home(request):
    return HttpResponse("<h1>Welcome to my portfolio site!</h1>")

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'main/project_list.html', {'projects': projects})
# Create your views here.
