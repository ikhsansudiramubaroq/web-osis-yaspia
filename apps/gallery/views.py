from django.shortcuts import render
from .models import Gallery, Category
from django.core.paginator import Paginator
from django.core.cache import cache

# Create your views here.

#Object Caching (best practice)
def gallery_list(request):
    # 1. Ambil Parameter dari URL
    category_name = request.GET.get('category') # Misal: 'Agama'
    page_number = request.GET.get('page', 1)

    # 2. BUAT CACHE KEY YANG UNIK (Penting!)
    # Kita tambahkan info kategori ke dalam nama key agar tidak tertukar
    cat_tag = category_name if category_name else "all"
    cache_key = f"gallery_data_{cat_tag}_page_{page_number}"

    # 3. Cek ke Upstash
    page_obj = cache.get(cache_key)

    if not page_obj:
        print(f"📡 Database: Menarik data gallery untuk kategori [{cat_tag}]...")
        
        # Query Dasar
        gallery_queryset = Gallery.objects.filter(status='publish') \
                                         .select_related('category') \
                                         .order_by('-created_at')

        # Filter berdasarkan Nama Kategori (karena tidak ada slug)
        current_category = None
        if category_name:
            # Kita filter berdasarkan field 'name' di model Category
            gallery_queryset = gallery_queryset.filter(category__name=category_name)
        
        # Pagination
        paginator = Paginator(gallery_queryset, 8)
        page_obj = paginator.get_page(page_number)

        # 4. Simpan ke Redis (900 detik = 15 menit)
        cache.set(cache_key, page_obj, 900)
    else:
        print(f"⚡ Cache: Menampilkan data [{cat_tag}] dari Upstash!")

    # Ambil daftar kategori untuk tombol filter di template
    categories = Category.objects.all()

    context = {
        'list_gallery': page_obj,
        'categories': categories,
        'current_category_name': category_name,
    }
    return render(request, 'gallery/galeri.html', context)
