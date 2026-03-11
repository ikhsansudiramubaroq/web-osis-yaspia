from django.shortcuts import render
from .models import Gallery,Category
from django.core.paginator import Paginator

# Create your views here.
def gallery_list(request):
    list_gallery = Gallery.objects.filter(status='publish') \
                                .select_related('category') \
                                .order_by('-created_at')
    paginator = Paginator(list_gallery, per_page = 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'list_gallery' : page_obj
    }
    return render(request, 'gallery/galeri.html', context)
