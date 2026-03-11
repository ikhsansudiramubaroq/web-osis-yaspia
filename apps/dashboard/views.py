from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import os
from news.models import News, Category
from gallery.models import Gallery, Category as cat_gal
from home.models import Hero, Visi, Misi, Agenda, Contact
from .forms import ActivityForm, GalleryForm, HeroForm, VisiForm, AgendaForm, ContactForm

# Create your views here.

@login_required # Hanya user login yang bisa akses dashboard
def dashboard_index(request):
    # Untuk dashboard_index, sebaiknya kirimkan statistik ringkas
    context = {
        'total_news': News.objects.count(),
        'total_gallery': Gallery.objects.count(),
    }
    return render(request, 'dashboard/index.html', context)

# --- MANAGE HOMEPAGE ---
@login_required # Hanya user login yang bisa akses dashboard
def manage_homepage(request):
    
    hero_list = Hero.objects.all().order_by('-created_at')
    #ambil data tunggal
    visi = Visi.objects.first()
    misi_list = Misi.objects.all()
    
    #data agenda untuk crud
    list_agenda = Agenda.objects.all().order_by('date_agenda')
    
    context = {
        'hero_list': hero_list,
        'visi': visi,
        'misi_list': misi_list,
        'list_agenda': list_agenda,
        'total_news': News.objects.count(),
        'total_gallery': Gallery.objects.count(),
    }
    return render(request, 'dashboard/homepage/homepage.html', context)

# --- EDIT HERO ---
def edit_hero(request, id):
    hero = get_object_or_404(Hero, id=id)
    if request.method == "POST":
        form = HeroForm(request.POST, request.FILES, instance=hero)
        if form.is_valid():
            # Best Practice: Hapus gambar lama jika upload baru
            if 'image_hero' in request.FILES and hero.image_hero:
                if os.path.isfile(hero.image_hero.path):
                    os.remove(hero.image_hero.path)
            form.save()
            return redirect('dashboard:manage_homepage')
    else:
        form = HeroForm(instance=hero)
    return render(request, 'dashboard/homepage/edit_hero.html', {'form': form, 'hero': hero})

# --- EDIT VISI & MISI ---
def edit_visi_misi(request):
   # Ambil atau buat data Visi (ID=1)
    visi, created = Visi.objects.get_or_create(id=1)
    misi_list = Misi.objects.all()
    
    if request.method == "POST":
        # Logika 1: Update Visi
        if 'update_visi' in request.POST:
            form = VisiForm(request.POST, request.FILES, instance=visi)
            if form.is_valid():
                form.save()
                messages.success(request, "Visi berhasil diperbarui!")
                return redirect('dashboard:edit_visi')
        
        # Logika 2: Tambah Misi Baru
        elif 'add_misi' in request.POST:
            teks_misi = request.POST.get('misi_baru')
            if teks_misi:
                Misi.objects.create(misi=teks_misi)
                messages.success(request, "Misi baru berhasil ditambahkan!")
            return redirect('dashboard:edit_visi')

    else:
        form = VisiForm(instance=visi)
        
    context = {
        'form': form,
        'visi': visi,
        'misi_list': misi_list
    }
    return render(request, 'dashboard/homepage/edit_visi.html', context)

# Fungsi tambahan untuk hapus misi lewat ID
def delete_misi(request, id):
    misi = get_object_or_404(Misi, id=id)
    misi.delete()
    messages.success(request, "Satu poin misi berhasil dihapus!")
    return redirect('dashboard:edit_visi')

# --- CRUD AGENDA ---
def add_agenda(request):
    form = AgendaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard:manage_homepage')
    return render(request, 'dashboard/homepage/add_agenda.html', {'form': form})

def edit_agenda(request, id):
    agenda = get_object_or_404(Agenda, id=id)
    form = AgendaForm(request.POST or None, instance=agenda)
    if form.is_valid():
        form.save()
        return redirect('dashboard:manage_homepage')
    return render(request, 'dashboard/homepage/edit_agenda.html', {'form': form})

def delete_agenda(request, id):
    agenda = get_object_or_404(Agenda, id=id)
    if request.method == "POST":
        agenda.delete()
    return redirect('dashboard:manage_homepage')

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
def detail_activity(request, slug):
    # Mengambil data berdasarkan slug untuk preview
    activity = get_object_or_404(News, slug=slug)
    
    context = {
        'activity': activity,
        'title': f"Preview: {activity.title}"
    }
    return render(request, 'dashboard/activity/detail_activity.html', context)

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
def detail_gallery(request, id):
    # Mengambil foto berdasarkan ID
    photo = get_object_or_404(Gallery, id=id)
    
    context = {
        'photo': photo,
        'title': "Detail Foto Gallery"
    }
    return render(request, 'dashboard/gallery/detail_gallery.html', context)

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

# --- MANAGE CONTACT ---
@login_required
def manage_contact(request):
    # Mengambil data pertama. Jika tabel kosong, Django akan buat data default
    contact, created = Contact.objects.get_or_create(id=1)

    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request, "Informasi Kontak berhasil diperbarui!")
            return redirect('dashboard:manage_contact')
    else:
        form = ContactForm(instance=contact)

    return render(request, 'dashboard/contact/manage_contact.html', {
        'form': form,
        'contact': contact
    })