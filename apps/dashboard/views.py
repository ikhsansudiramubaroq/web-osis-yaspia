from django.shortcuts import render, redirect, get_object_or_404
from news.models import News, Category
from gallery.models import Gallery, Category as cat_gal
from django.contrib.auth.decorators import login_required
from .forms import ActivityForm, GalleryForm
from django.contrib import messages
import os
from django.conf import settings

# Create your views here.

@login_required # Hanya user login yang bisa akses dashboard
def dashboard_index(request):
    # Untuk dashboard_index, sebaiknya kirimkan statistik ringkas
    context = {
        'total_news': News.objects.count(),
        'total_gallery': Gallery.objects.count(),
    }
    return render(request, 'dashboard/index.html', context)

# --- ACTIVITY SECTION ---
@login_required
def list_activity(request):
    activity = News.objects.select_related('category').all().order_by('-created_at')
    
    context = {
        'list_activity' : activity
    }
    return render (request, 'dashboard/activity/list_activity.html', context)

@login_required
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

@login_required
def edit_activity(request, slug):
    # Mengambil data lama berdasarkan slug
    activity = get_object_or_404(News, slug=slug)
    
    if request.method == "POST":
        # instance=activity memberitahu Django kita mengedit data yang sudah ada
        form = ActivityForm(request.POST, request.FILES, instance=activity)
        if form.is_valid():
            form.save()
            messages.success(request, "Kegiatan berhasil diperbarui!")
            return redirect('dashboard:list_activity')
    else:
        form = ActivityForm(instance=activity)
    
    return render(request, 'dashboard/activity/edit_activity.html', {'form': form, 'activity': activity})

@login_required
def delete_activity(request, slug):
    activity = get_object_or_404(News, slug=slug)
    if request.method == "POST":
        # Hapus file fisik gambar jika ada
        if activity.image:
            if os.path.isfile(activity.image.path):
                os.remove(activity.image.path)
        
        activity.delete()
        messages.success(request, "Kegiatan berhasil dihapus!")
        return redirect('dashboard:list_activity')
    return redirect('dashboard:list_activity')

# -- GALLERY SECTION --
@login_required
def list_gallery(request):
    gallery = Gallery.objects.select_related('category').all().order_by('-created_at')
    
    context = {
        'list_gallery' : gallery
    }
    return render (request, 'dashboard/gallery/list_gallery.html', context)

@login_required
def add_gallery(request):
    if request.method == "POST":
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Foto berhasil ditambahkan !")
            return redirect('dashboard:list_gallery')
        else:
            messages.error(request, "Terjadi kesalahan saat menambahkan Foto")
    else:
        form = GalleryForm()
    
    categories = cat_gal.objects.all()
    context = {
        'categories' : categories,
        'form' : form
    }
    return render(request, 'dashboard/gallery/add_gallery.html', context)

@login_required
def edit_gallery(request, id):
    # Mengambil data lama berdasarkan ID
    gallery = get_object_or_404(Gallery, id=id)
    
    if request.method == "POST":
        form = GalleryForm(request.POST, request.FILES, instance=gallery)
        if form.is_valid():
            form.save()
            messages.success(request, "Foto gallery berhasil diperbarui!")
            return redirect('dashboard:list_gallery')
    else:
        form = GalleryForm(instance=gallery)
    
    return render(request, 'dashboard/gallery/edit_gallery.html', {'form': form, 'gallery': gallery})

@login_required
def delete_gallery(request, id):
    gallery = get_object_or_404(Gallery, id=id)
    if request.method == "POST":
        if gallery.image:
            if os.path.isfile(gallery.image.path):
                os.remove(gallery.image.path)
        
        gallery.delete()
        messages.success(request, "Foto gallery berhasil dihapus!")
        return redirect('dashboard:list_gallery')
    return redirect('dashboard:list_gallery')