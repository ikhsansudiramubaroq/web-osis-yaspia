from django.shortcuts import render
from .models import Gallery
from django.core.paginator import Paginator
from django.core.cache import cache

# Create your views here.

#Object Caching (best practice)
def gallery_list(request):
    page_number = request.GET.get('page', 1)
    
    #buat (key) berdasarkan nomer halaman
    cache_key = f'gallery_data_page_{page_number}'
    
    # 1. coba ambil data dari cache upstash
    page_obj = cache.get(cache_key)
    
    if not page_obj:
        # Jika Kosong, baru tanya Database (Hanya jalan sekali tiap 15 menit)
        list_gallery = Gallery.objects.filter(status='publish') \
                                    .select_related('category') \
                                    .order_by('-created_at')
                                    
        paginator = Paginator(list_gallery, per_page = 8)
        page_obj = paginator.get_page(page_number)
        
        # 3. Simpan hasilnya ke Cache selama 15 menit (900 detik)
        cache.set(cache_key, page_obj, 900)
    else:
        print("⚡ Data diambil dari Cache Upstash!")
    
    context = {
        'list_gallery' : page_obj
    }
    return render(request, 'gallery/galeri.html', context)
