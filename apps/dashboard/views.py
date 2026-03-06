from django.shortcuts import render, redirect
from news.models import News, Category
from .forms import ActivityForm
from django.contrib import messages

# Create your views here.
def dashboard_index(request):
    return render (request, 'dashboard/index.html')

# activity
def list_activity(request):
    activity = News.objects.all()
    
    context = {
        'list_activity' : activity
    }
    return render (request, 'dashboard/activity/list_activity.html', context)
def add_activity(request):
    if request.method == "POST":
        form = ActivityForm(request.POST, request.FILES)
        if form.is_valid():
            new_activity = form.save(commit=False)
            new_activity.author = request.user
            new_activity.save()
            messages.success(request, "Kegiatan berhasil ditambahkan !")
            return redirect('dashboard:list_activity')
        else:
            messages.error(request, "Terjadi kesalahan saat menambahkan Kegiatan")
    else:
        form = ActivityForm()
    
    categories = Category.objects.all()
    context = {
        'categories' : categories,
        'form' : form
    }
    return render(request, 'dashboard/activity/add_activity.html', context)

# gallery
def list_gallery(request):
    return render (request, 'dashboard/gallery/list_gallery.html')