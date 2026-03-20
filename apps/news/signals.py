from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from .models import News

@receiver([post_save, post_delete], sender=News)
def hapus_cache_news(sender, instance, **kwargs):
    # hapus cache khusus gallery saja
    cache.delete_pattern('news_data_*')
    # Hapus juga cache data home yang mengandung gallery
    cache.delete('home_data_all')
    
    cache.clear()
    print(f"🧹 SIGNAL: Cache Bersih! Perubahan pada berita: {instance.title}")