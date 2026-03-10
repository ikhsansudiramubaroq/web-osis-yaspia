from django import forms
from news.models import News
from gallery.models import Gallery
from home.models import Hero, Agenda, Visi, Misi

class HeroForm(forms.ModelForm):
    class Meta:
        model = Hero
        fields = ['title_hero', 'subtitle_hero', 'image_hero']
        widgets = {
            'title_hero': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitle_hero': forms.TextInput(attrs={'class': 'form-control'}),
            'image_hero': forms.FileInput(attrs={'class': 'form-control'}),
        }

class VisiForm(forms.ModelForm):
    class Meta:
        model = Visi
        fields = ['teks_visi', 'description_image', 'image_visi']
        widgets = {
            'teks_visi': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'description_image': forms.TextInput(attrs={'class': 'form-control'}),
            'image_visi': forms.FileInput(attrs={'class': 'form-control'}),
        }

class AgendaForm(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = '__all__'
        widgets = {
            'title_agenda': forms.TextInput(attrs={'class': 'form-control'}),
            'category_agenda': forms.TextInput(attrs={'class': 'form-control'}),
            'description_agenda': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'date_agenda': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'time_agenda': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'status_agenda': forms.Select(attrs={'class': 'form-select'}),
        }

class ActivityForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Menambahkan empty label (placeholder) untuk dropdown kategori
        self.fields['category'].empty_label = "--- Pilih Kategori Kegiatan ---"
        
    class Meta:
        model = News
        # Kita tidak masukkan 'author' dan 'slug' karena diisi otomatis
        fields = ['title', 'category', 'content', 'status', 'image']
        
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control form-control-lg', 
                'placeholder': 'Masukkan judul kegiatan...'
            }),
            'category': forms.Select(attrs={
                'class': 'form-select form-select-lg',
                }),
            'status': forms.RadioSelect(attrs={
                'class': 'form-check-input',
            }),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 10:
            raise forms.ValidationError("Judul terlalu pendek, minimal 10 karakter.")
        return title


class GalleryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Menambahkan empty label (placeholder) untuk dropdown kategori
        self.fields['category'].empty_label = "--- Pilih Kategori Gallery ---"
        
    class Meta:
        model = Gallery
        # Kita tidak masukkan 'author' dan 'slug' karena diisi otomatis
        fields = ['title', 'category', 'status', 'description', 'image']
        
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control form-control-lg', 
                'placeholder': 'Masukkan judul gallery...'
            }),
            'category': forms.Select(attrs={
                'class': 'form-select form-select-lg',
                }),
            'status': forms.RadioSelect(attrs={
                'class': 'form-check-input',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Tuliskan deskripsi singkat mengenai foto ini...',
                'rows': 4, # Menentukan tinggi awal kotak teks
            }),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 10:
            raise forms.ValidationError("Judul terlalu pendek, minimal 10 karakter.")
        return title