from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dashboard_index(request):
    return HttpResponse("<h1>Ini halaman dashboard admin</h1>")