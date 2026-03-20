from django.db import models
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill
from django.conf import settings

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,blank=True, editable=False)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name
            

class News(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('publish', 'Publish')
    ]
    
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='news')
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True,blank=True, editable=False)
    content = CKEditor5Field('Content', config_name='extends')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    
    # untuk detail news 
    image = ProcessedImageField(
        upload_to='news_pics/%Y/%m/%d/',
        processors=[ResizeToFill(1200,675)],
        format='JPEG', #format otomatis diubah ke jpeg semua
        options={'quality':80}, #mengecilkan 80%
        null=True,blank=True
    )
    
    # Ini otomatis mengecilkan gambar di atas tanpa kamu upload lagi
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(400, 225)], # Ukuran kecil untuk list/thumbnail
        format='JPEG',
        options={'quality': 70}
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.title