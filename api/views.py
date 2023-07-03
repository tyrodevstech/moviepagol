from itertools import chain
from app_main.models import *
from django.http import JsonResponse
from tmdbv3api import TMDb,Movie,TV,Trending
tmdb = TMDb()
apiKey = 'c922683661639d2817db046e73983d60'
tmdb.api_key = apiKey
movie = Movie()
series = TV()

# Create your views here.
def getSearchTMDBMoviesData(request):
    contentTitle = request.POST.get('contentTitle')
    search = movie.search(contentTitle)
    contentsList = []
    for res in search:
        contentsList.append(dict(res))

    context = {
        'status':1,
        'contentsInfos':contentsList,
    }
    return JsonResponse(context,safe=False)


def getSearchTMDBSeriesData(request):
    contentTitle = request.POST.get('contentTitle')
    search = series.search(contentTitle)
    contentsList = []
    for res in search:
        contentsList.append(dict(res))

    context = {
        'status':1,
        'contentsInfos':contentsList,
    }
    return JsonResponse(context,safe=False)


def getSearchContent(request):
    title = request.GET.get('title')
    movieobjs = MovieModel.objects.filter(title__icontains = title)
    seriseobjs = SeriesModel.objects.filter(title__icontains = title)
    softgameobjs = SoftwaresGamesModel.objects.filter(title__icontains = title)
    data = list(chain(movieobjs.values(), seriseobjs.values(),softgameobjs.values()))
    if data:
        content = {
            'status':1,
            'movieobjs':list(movieobjs.values())[:25],
            'seriseobjs':list(seriseobjs.values())[:25],
            'softgameobjs':list(softgameobjs.values())[:25]
        }
    else:
        content = {
            'status':0,
        }
    return JsonResponse(content)



def getSeasonModelData(request,seasonId):
    obj = SeasonModel.objects.get(id=seasonId)
    if obj and obj.series.tmdbid:
        context = {
            'status':1,
            'seasonNum':obj.season_number,
            'seriesTmdbId':obj.series.tmdbid,
        }
    else:
        context = {
            'status':0,
        }
    return JsonResponse(context,safe=False)

