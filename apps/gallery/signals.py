from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from .models import Gallery

@receiver([post_save, post_delete], sender=Gallery)
def hapus_cache_gallery(sender, instance, **kwargs):
    # Gunakan clear() dulu supaya PASTI berhasil untuk View Cache & Object Cache
    cache.clear()
    print(f"🧹 SIGNAL: Cache Bersih! Perubahan pada foto: {instance.title}")