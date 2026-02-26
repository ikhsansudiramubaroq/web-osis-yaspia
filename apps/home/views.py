from django.shortcuts import render
from .models import Hero,Agenda,Visi,Misi,Contact
from gallery.models import Gallery

# Create your views here.
def home_index(request):
    gallery = Gallery.objects.all()[:6]
    hero = Hero.objects.all()
    agenda = Agenda.objects.all()
    visi = Visi.objects.first() # Mengambil data pertama/satu-satunya
    misi = Misi.objects.all()
    
    context = {
        'agenda' : agenda,
        'visi' : visi,
        'misi' : misi,
        'hero': hero,
        'home_gallery' : gallery
    }
    
    return render(request, 'home/index.html', context)