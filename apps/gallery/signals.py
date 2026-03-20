from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from .models import Gallery

@receiver([post_save, post_delete], sender=Gallery)
def hapus_cache_gallery(sender, instance,**kwargs):
    # hapus cache khusus gallery saja
    cache.delete_pattern('gallery_data_*')
    # Hapus juga cache data home yang mengandung gallery
    cache.delete('home_data_all')
    
    cache.clear()
    print(f"🧹 SIGNAL: Cache Bersih! Perubahan pada foto: {instance.title}")