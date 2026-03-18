from django.shortcuts import render
from .models import Hero,Agenda,Visi,Misi,Contact
from gallery.models import Gallery
from news.models import News
from django.core.cache import cache

# Create your views here.

# object caching agar proses render template base.html dan footer tetap di render tanpa gangguan caching
def home_index(request):
    # simpan semua data home dalam satu kunci besar agar irit query
    cache_key = 'home_data_all'
    context = cache.get(cache_key)
    
    if not context:
        context = {
            'home_gallery' : Gallery.objects.filter(status='publish').order_by('-created_at')[:4],
            'home_news' : News.objects.filter(status ='publish')[:3],
            'hero' : Hero.objects.all().order_by('-created_at'),
            'agenda' : Agenda.objects.filter(status_agenda = 'publish').order_by('-date_agenda'),
            'visi' : Visi.objects.first(), # Mengambil data pertama/satu-satunya
            'misi' : Misi.objects.all(),
        }
        
        # Simpan ke Upstash
        cache.set(cache_key, context, 60 * 15)
    
    return render(request, 'home/index.html', context)