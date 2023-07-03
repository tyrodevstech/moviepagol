from .models import GenreModel
from django.conf import settings
def site(request):
    return {'SITE_URL': settings.SITE_URL}

def servemodels(request):
    genres = GenreModel.objects.all()
    list_item = 10
    genresList = [genres[i:i+list_item] for i in range(0,len(genres),list_item)]
    context = {
        'genresList':genresList
    }
    return context