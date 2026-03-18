from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache

# Import semua model yang datanya nampang di Home
from home.models import Hero, Agenda, Visi, Misi
from gallery.models import Gallery
from news.models import News

# Kita buat satu fungsi pembersih untuk semua model di atas
@receiver([post_save, post_delete], sender=Hero)
@receiver([post_save, post_delete], sender=Agenda)
@receiver([post_save, post_delete], sender=Visi)
@receiver([post_save, post_delete], sender=Misi)
@receiver([post_save, post_delete], sender=Gallery)
@receiver([post_save, post_delete], sender=News)

def clear_home_cache(sender, instance, **kwargs):
    """
    Tujuannya satu: Hapus cache 'home_data_all' 
    siapa pun yang berubah di antara model di atas.
    """
    cache.delete('home_data_all')
    print(f"🏠 SIGNAL HOME: Cache utama dihapus karena perubahan pada {sender.__name__}")