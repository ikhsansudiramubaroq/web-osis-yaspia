from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dashboard_index(request):
    return render (request, 'dashboard/index.html')

# activity
def list_activity(request):
    return render (request, 'dashboard/activity/list_activity.html')

# gallery
def list_gallery(request):
    return render (request, 'dashboard/gallery/list_gallery.html')