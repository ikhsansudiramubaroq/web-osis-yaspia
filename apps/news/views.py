from django.shortcuts import render, get_object_or_404
from .models import News
from django.core.paginator import Paginator

# Create your views here.

# Create your views here.
def news_list(request) :
    news_list = News.objects.all() #tampilkan query data
    paginator = Paginator(news_list,per_page = 6 ) # Class Paginator berisi param(query data, brp data yg tampil)
    page_number = request.GET.get('page') #ambil 'page' sesuai dengan klik halaman 
    page_obj = paginator.get_page(page_number) #get_page ambil number page ke berapa
    
    context = {
        'news_list' : page_obj,
    }
    return render(request, 'news/berita.html', context)

def detail_news(request, slug_news):
    # Gunakan .only() untuk Postgres agar tidak membebani memory (ambil field yang perlu saja)
    news_item = get_object_or_404(
        News.objects.select_related('category', 'user').only(
            'title', 'content', 'image', 'created_at', 
            'category__name', 'user__username'
        ),
        slug=slug_news
    )

    # 2. Siapkan context
    context = {
        'news_detail': news_item, # Ini variabel yang dipanggil di template
    }
    
    return render (request, 'news/detail-berita.html', context)