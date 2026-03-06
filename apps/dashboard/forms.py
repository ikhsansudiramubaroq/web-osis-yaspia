from django import forms
from news.models import News

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