from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from .models import News

@receiver([post_save, post_delete], sender=News)
def hapus_cache_news(sender, instance, **kwargs):
    # hapus cache khusus news saja
    cache.delete_pattern('news_data_page_*')
    # Hapus juga cache data home yang mengandung news
    cache.delete('home_data_all')
    print(f"🧹 SIGNAL: Cache Bersih! Perubahan pada berita: {instance.title}")