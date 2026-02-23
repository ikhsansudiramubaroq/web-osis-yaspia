from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Gallery(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    
    # untuk detail gallery 
    image = ProcessedImageField(
        upload_to='news_pics/%Y/%m/%d/',
        processors=[ResizeToFill(1200,675)],
        format='JPEG', #format otomatis diubah ke jpeg semua
        options={'quality':80}, #mengecilkan 80%
        null=True,blank=True
    )
    
    # untuk thumbnail gallery
    image_thumbnail = ImageSpecField(
        source='image',
        processors= [ResizeToFill(400,255)],
        format='JPEG',
        options={'quality':70}
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title