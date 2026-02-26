from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.
class Hero(models.Model):
    title_hero = models.CharField(max_length=100)
    subtitle_hero = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    image_hero = ProcessedImageField(
        upload_to='hero/',
        processors=[ResizeToFill(1200, 675)],
        format='JPEG',
        options={'quality': 80}
    )

    def __str__(self):
        return self.title_hero

class Agenda(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('publish', 'Publish')
    ]
    title_agenda = models.CharField(max_length=100)
    category_agenda = models.CharField(max_length=50)
    description_agenda = models.TextField()
    location = models.CharField(max_length=50)
    date_agenda = models.DateField()
    time_agenda = models.TimeField()
    status_agenda = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='draft'
    )
    
    def __str__(self):
        return self.title_agenda

class Visi(models.Model):
    # Field Visi (Biasanya teksnya panjang)
    teks_visi = models.TextField()
    description_image = models.CharField(max_length=50)
    
    image_visi = ProcessedImageField(
        upload_to='visi/',
        processors=[ResizeToFill(600, 400)],
        format='JPEG',
        options={'quality': 80}
    )
    
    def __str__(self):
        return "Visi Sekolah Yaspia"

class Misi(models.Model):
    misi = models.CharField(max_length=255)
        
    def __str__(self):
        return self.misi

class Contact(models.Model):
    email_school = models.EmailField()
    telp_school = models.CharField(max_length=20)
    address_school = models.TextField
    google_maps = models.TextField(help_text="Masukkan embed link dari Google Maps")
    
    # social media
    instagram = models.URLField(blank=True,null=True)
    yotube = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return "Kontak Sekolah"