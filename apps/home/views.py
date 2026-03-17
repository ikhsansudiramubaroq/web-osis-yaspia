from django.shortcuts import render
from .models import Hero,Agenda,Visi,Misi,Contact
from gallery.models import Gallery
from news.models import News
from django.views.decorators.cache import cache_page

# Create your views here.
@cache_page(60 * 15)
def home_index(request):
    gallery = Gallery.objects.filter(status='publish')[:4]
    news = News.objects.filter(status ='publish')[:3]
    hero = Hero.objects.all()
    agenda = Agenda.objects.filter(status_agenda = 'publish')
    visi = Visi.objects.first() # Mengambil data pertama/satu-satunya
    misi = Misi.objects.all()
    
    context = {
        'agenda' : agenda,
        'visi' : visi,
        'misi' : misi,
        'hero': hero,
        'home_gallery' : gallery,
        'home_news' : news,
    }
    
    return render(request, 'home/index.html', context)