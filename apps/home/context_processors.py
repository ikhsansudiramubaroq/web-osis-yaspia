from .models import Contact

def contact_renderer(request):
    # Mengambil data kontak pertama dari database
    return {
        'contact': Contact.objects.first()
    }