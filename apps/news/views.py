from django.shortcuts import render
from .models import News

# Create your views here.
def news_list(request) :
    return render(request, 'news/berita.html')

# Create your views here.
def news_detail(request) :
    news_list = News.objects.all()
    
    context = {
        'news_list' : news_list,
    }
    return render(request, 'news/detail-berita.html', context)