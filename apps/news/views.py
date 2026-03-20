from django.shortcuts import render, get_object_or_404
from .models import News, Category
from django.core.paginator import Paginator
from django.core.cache import cache

# Create your views here.

# Create your views here.
def news_list(request) :
    # 1. Ambil Parameter dari URL
    category_slug = request.GET.get('category') # Misal: 'Agama'
    page_number = request.GET.get('page', 1)
    
    # 2. BUAT CACHE KEY YANG UNIK (Penting!)
    # Kita tambahkan info kategori ke dalam nama key agar tidak tertukar
    cat_tag = category_slug if category_slug else "all"
    cache_key = f"news_data_{cat_tag}_page_{page_number}"
    
    # 3. Cek ke Upstash
    page_obj = cache.get(cache_key)
    
    if not page_obj:
        print(f"📡 Database: Menarik data news untuk kategori [{cat_tag}]...")
        news_list = News.objects.filter(status='publish') \
                            .select_related('category', 'author') \
                            .order_by('-created_at')
    
        # Jika ada filter kategori, saring datanya
        if category_slug:
            news_list = news_list.filter(category__slug = category_slug)
            
        paginator = Paginator(news_list, 6 ) # Class Paginator berisi param(query data, brp data yg tampil)
        page_obj = paginator.get_page(page_number) #get_page ambil number page ke berapa
        
        # 4. Simpan ke Redis (900 detik = 15 menit)
        cache.set(cache_key, page_obj, 900)
    else:
        print(f"⚡ Cache: Menampilkan data [{cat_tag}] dari Upstash!")
        
    # Ambil semua kategori untuk ditampilkan di tombol filter
    categories = Category.objects.all()
    
    context = {
        'news_list' : page_obj,
        'categories' : categories,
        'current_category_slug' : category_slug,
    }
    return render(request, 'news/berita.html', context)

def detail_news(request, slug_news):
    # Gunakan .only() untuk Postgres agar tidak membebani memory (ambil field yang perlu saja)
    news_item = get_object_or_404(
        News.objects.select_related('category', 'author').only(
            'title', 'content', 'image', 'created_at', 
            'category__name', 'author__first_name'
        ),
        slug=slug_news,
        status = 'publish'
    )

    # 2. Siapkan context
    context = {
        'news_detail': news_item, # Ini variabel yang dipanggil di template
    }
    
    return render (request, 'news/detail-berita.html', context)