import random
from itertools import chain
from urllib.parse import *

from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render

from app_main.models import *


# Create your views here.
def index(request):
    topsliderobjs = sorted(
        TopSlideModel.objects.filter(), key=lambda x: random.random()
    )
    topmovieobjs = MovieModel.objects.filter().order_by("-created_at")[:20]
    engmovieobjs = MovieModel.objects.filter(type="english").order_by("-created_at")
    frgmovieobjs = MovieModel.objects.filter(
        Q(type="korean")
        | Q(type="spanish")
        | Q(type="japanese")
        | Q(type="turkish")
        | Q(type="chinese")
        | Q(type="thai")
        | Q(type="russian")
        | Q(type="indonesian")
        | Q(type="iranian")
        | Q(type="french")
        | Q(type="german")
        | Q(type="others")
    ).order_by("-created_at")
    hindimovieobjs = MovieModel.objects.filter(type="hindi").order_by("-created_at")
    southmovieobjs = MovieModel.objects.filter(
        Q(type="malayalam") | Q(type="tamil") | Q(type="telugu") | Q(type="kannada")
    ).order_by("-created_at")
    bsubobjs = BSubModel.objects.filter().order_by("-movie_content__created_at")
    seriesobjs = (
        SeriesModel.objects.filter()
        .order_by("-created_at")
        .exclude(Q(type="korean") | Q(type="anime"))
    )
    kdramaobjs = SeriesModel.objects.filter(type="korean").order_by("-created_at")

    animationobjs = MovieModel.objects.filter(type="animation").order_by("-created_at")
    noticeqs = Notice.objects.all()[:5]
    context = {
        "topsliderobjs": topsliderobjs,
        "topmovieobjs": topmovieobjs,
        "notices": noticeqs,


        "bsubobjs": bsubobjs[:20],
        "bsub_count": bsubobjs.count(),

        "hindimovieobjs": hindimovieobjs[:20],
        "hindimovies_count": hindimovieobjs.count(),

        "southmovieobjs": southmovieobjs[:20],
        "southmovies_count": southmovieobjs.count,

        "engmovieobjs": engmovieobjs[:20],
        "engmovies_count": engmovieobjs.count(),

        "frgmovieobjs": frgmovieobjs[:20],
        "frgmovies_count": frgmovieobjs.count(),

        "seriesobjs": seriesobjs[:20],
        "series_count": seriesobjs.count(),

        "kdramaobjs": kdramaobjs[:20],
        "kdrama_count": kdramaobjs.count(),

        "animationobjs": animationobjs[:20],
        "animation_count": animationobjs.count(),
    }
    return render(request, "app_main/index.html", context)


def movies_view(request, type):
    if type == "foreign":
        movies = MovieModel.objects.filter(
            Q(type="korean")
            | Q(type="spanish")
            | Q(type="japanese")
            | Q(type="turkish")
            | Q(type="chinese")
            | Q(type="thai")
            | Q(type="russian")
            | Q(type="indonesian")
            | Q(type="iranian")
            | Q(type="french")
            | Q(type="german")
            | Q(type="others")
        ).order_by("-created_at")
    elif type == "south_indian":
        movies = MovieModel.objects.filter(
            Q(type="malayalam") | Q(type="tamil") | Q(type="telugu") | Q(type="kannada")
        ).order_by("-created_at")
    else:
        movies = MovieModel.objects.filter(type=type).order_by("-created_at")
    paginator = Paginator(movies, 24)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "movies": page_obj,
        "type": type,
        "totalobj": movies.count,
    }
    return render(request, "app_main/all/movies.html", context)


def series_view(request, type):
    if type == "all":
        series = (
            SeriesModel.objects.filter().order_by("-created_at").exclude(type="korean")
        )
    elif type == "indian":
        series = SeriesModel.objects.filter(
            Q(type="malayalam")
            | Q(type="hindi")
            | Q(type="tamil")
            | Q(type="telugu")
            | Q(type="kannada")
        ).order_by("-created_at")
    elif type == "foreign":
        series = SeriesModel.objects.filter(
            Q(type="spanish")
            | Q(type="japanese")
            | Q(type="turkish")
            | Q(type="chinese")
            | Q(type="thai")
            | Q(type="russian")
            | Q(type="indonesian")
            | Q(type="iranian")
            | Q(type="french")
            | Q(type="german")
            | Q(type="others")
        ).order_by("-created_at")
    else:
        series = SeriesModel.objects.filter(type=type).order_by("-created_at")

    paginator = Paginator(series, 24)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "series": page_obj,
        "type": type,
        "totalobj": series.count,
    }
    return render(request, "app_main/all/series.html", context)


def softwaresGames_view(request, category):
    softwaresGames = SoftwaresGamesModel.objects.filter(category=category).order_by(
        "-created_at"
    )
    paginator = Paginator(softwaresGames, 24)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "softwaresGames": page_obj,
        "category": category,
        "totalobj": softwaresGames.count,
    }
    return render(request, "app_main/all/softwaresgames.html", context)


def genres_view(request, genrename):
    genrename = unquote(genrename)
    movies = MovieModel.objects.filter(genre__genre_name__icontains=genrename).order_by(
        "-created_at"
    )
    paginator = Paginator(movies, 24)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "movies": page_obj,
        "genrename": genrename,
        "totalobj": movies.count,
    }
    return render(request, "app_main/all/genres.html", context)


def classic_view(request, type):
    classicmovies = ClassicModel.objects.filter(type=type)
    paginator = Paginator(classicmovies, 24)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "classicmovies": page_obj,
        "type": type,
        "totalobj": classicmovies.count,
    }
    return render(request, "app_main/all/classic.html", context)


def dualaudio_view(request):
    dualaudiomovies = DualAudioModel.objects.all()
    paginator = Paginator(dualaudiomovies, 24)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "dualaudiomovies": page_obj,
        "totalobj": dualaudiomovies.count,
    }
    return render(request, "app_main/special/dual_audio.html", context)


def bsub_view(request):
    bsubmovies = BSubModel.objects.all()
    paginator = Paginator(bsubmovies, 24)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "bsubmovies": page_obj,
        "totalobj": bsubmovies.count,
    }
    return render(request, "app_main/special/bsub.html", context)


def hindidubbed_view(request):
    hindidubbedmovies = HindiDubbedModel.objects.all()
    paginator = Paginator(hindidubbedmovies, 24)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "hindidubbedmovies": page_obj,
        "totalobj": hindidubbedmovies.count,
    }
    return render(request, "app_main/special/hindi_dubbed.html", context)


def satyajitray_view(request):
    satyajitraymovies = SatyajitRayModel.objects.all()
    paginator = Paginator(satyajitraymovies, 24)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "satyajitraymovies": page_obj,
        "totalobj": satyajitraymovies.count,
    }
    return render(request, "app_main/special/satyajitray.html", context)


def jamesbond_view(request):
    jamesbondmovies = JamesBondModel.objects.all()
    paginator = Paginator(jamesbondmovies, 24)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "jamesbondmovies": page_obj,
        "totalobj": jamesbondmovies.count,
    }
    return render(request, "app_main/special/jamesbond.html", context)


def oscarwinning_view(request):
    oscarwinningmovies = OscarWinningModel.objects.all()
    paginator = Paginator(oscarwinningmovies, 24)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "oscarwinningmovies": page_obj,
        "totalobj": oscarwinningmovies.count,
    }
    return render(request, "app_main/special/oscarwinning.html", context)


def imdbtop_view(request):
    imdbtopmovies = IMDBTopModel.objects.all()
    paginator = Paginator(imdbtopmovies, 24)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "imdbtopmovies": page_obj,
        "totalobj": imdbtopmovies.count,
    }
    return render(request, "app_main/special/imdbtop.html", context)


def superhero_view(request):
    superheromovies = SuperheroModel.objects.all()
    paginator = Paginator(superheromovies, 24)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "superheromovies": page_obj,
        "totalobj": superheromovies.count,
    }
    return render(request, "app_main/special/superhero.html", context)


def foundFootage_view(request):
    footages = FootageModel.objects.all()
    paginator = Paginator(footages, 24)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "footages": page_obj,
        "totalobj": footages.count,
    }
    return render(request, "app_main/special/footage.html", context)


# from meta.views import Meta


def details_movie_view(request, pk):
    obj = MovieModel.objects.get(slug=pk)
    recobjs = sorted(
        MovieModel.objects.filter(type=obj.type).order_by("-created_at")[:12],
        key=lambda x: random.random(),
    )
    context = {
        "obj": obj,
        "recobjs": recobjs,
    }
    return render(request, "app_main/details/details_movie.html", context)


def director_contents_view(request, directorName):
    directorName = unquote(directorName)
    movies = MovieModel.objects.filter(director__icontains=directorName).order_by(
        "-created_at"
    )
    paginator = Paginator(movies, 24)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "movies": page_obj,
        "director": directorName,
        "totalobj": movies.count,
    }
    return render(request, "app_main/all/director_contents.html", context)


def writer_contents_view(request, writerName):
    writerName = unquote(writerName)
    movies = MovieModel.objects.filter(writers__icontains=writerName).order_by(
        "-created_at"
    )
    paginator = Paginator(movies, 24)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "movies": page_obj,
        "writer": writerName,
        "totalobj": movies.count,
    }
    return render(request, "app_main/all/writer_contents.html", context)


def actor_contents_view(request, actorName):
    actorName = unquote(actorName)
    movies = MovieModel.objects.filter(starring__icontains=actorName).order_by(
        "-created_at"
    )
    paginator = Paginator(movies, 24)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "movies": page_obj,
        "actor": actorName,
        "totalobj": movies.count,
    }
    return render(request, "app_main/all/actor_contents.html", context)


def bsubcreator_contents_view(request, creatorSlug):
    movies = MovieModel.objects.filter(bsub_creator__slug=creatorSlug).order_by(
        "-created_at"
    )
    series = SeriesModel.objects.filter(bsub_creator__slug=creatorSlug).order_by(
        "-created_at"
    )
    creator = BsubCreatorModel.objects.filter(slug=creatorSlug)[0]
    objs = sorted(list(chain(movies, series)), key=lambda x: random.random())
    paginator = Paginator(objs, 24)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "movies": page_obj,
        "creator": creator,
        "totalobj": objs.__len__,
    }
    return render(request, "app_main/all/bsubcreator_contents.html", context)


def details_series_view(request, pk):
    obj = SeriesModel.objects.get(slug=pk)
    seasons = SeasonModel.objects.filter(series__slug=pk)
    recobjs = sorted(
        SeriesModel.objects.filter(type=obj.type).order_by("-created_at")[:12],
        key=lambda x: random.random(),
    )
    context = {"obj": obj, "seasons": seasons, "recobjs": recobjs}
    return render(request, "app_main/details/details_series.html", context)


def details_season_view(request, pk):
    obj = SeasonModel.objects.get(id=pk)
    episodes = EpisodeModel.objects.filter(season__id=pk)
    recobjs = sorted(
        SeasonModel.objects.filter(series__type=obj.series.type).order_by(
            "-created_at"
        )[:12],
        key=lambda x: random.random(),
    )
    context = {"obj": obj, "episodes": episodes, "recobjs": recobjs}
    return render(request, "app_main/details/details_season.html", context)


def details_softwaresGames_view(request, category, pk):
    obj = SoftwaresGamesModel.objects.get(slug=pk)
    recobjs = sorted(
        SoftwaresGamesModel.objects.filter(category=category).order_by("-created_at")[
            :12
        ],
        key=lambda x: random.random(),
    )
    context = {"obj": obj, "recobjs": recobjs}
    return render(request, "app_main/details/details_softwaresgames.html", context)


def search_view(request):
    title = request.GET.get("q")
    movies = (
        MovieModel.objects.filter(title__icontains=title)
        .exclude(Q(type="animation") | Q(type="anime"))
        .order_by("-created_at")[:25]
    )
    series = (
        SeriesModel.objects.filter(title__icontains=title)
        .exclude(Q(type="korean") | Q(type="anime"))
        .order_by("-created_at")[:25]
    )
    animationobjs = (
        MovieModel.objects.filter(title__icontains=title)
        .filter(type="animation")
        .order_by("-created_at")[:25]
    )
    animemovieobjs = (
        MovieModel.objects.filter(title__icontains=title)
        .filter(type="anime")
        .order_by("-created_at")[:25]
    )
    animeseriesobjs = (
        SeriesModel.objects.filter(title__icontains=title)
        .filter(type="anime")
        .order_by("-created_at")[:25]
    )
    kdramaobjs = (
        SeriesModel.objects.filter(title__icontains=title)
        .filter(type="korean")
        .order_by("-created_at")[:25]
    )
    softwares = (
        SoftwaresGamesModel.objects.filter(title__icontains=title)
        .exclude(category="games")
        .order_by("-created_at")[:25]
    )
    games = (
        SoftwaresGamesModel.objects.filter(title__icontains=title)
        .exclude(category="softwares")
        .order_by("-created_at")[:25]
    )
    context = {
        "searched": title,
        "movieobjs": movies,
        "seriesobjs": series,
        "animationobjs": animationobjs,
        "animemovieobjs": animemovieobjs,
        "animeseriesobjs": animeseriesobjs,
        "kdramaobjs": kdramaobjs,
        "softwaresobjs": softwares,
        "gamesobjs": games,
    }
    return render(request, "app_main/search.html", context)


from django.apps import apps


def contactus_view(request):
    return render(request, "app_main/extras/contactus.html")


def aboutus_view(request):
    return render(request, "app_main/extras/aboutus.html")


def privacy_view(request):
    return render(request, "app_main/extras/privacy.html")


def fileserver_view(request):
    return render(request, "app_main/fileserver.html")


# custom error handling page
def custom_page_not_found_view(request, exception=None):
    return render(request, "custom_error_page/404.html", {})


def custom_error_view(request, exception=None):
    return render(request, "custom_error_page/500.html", {})


def custom_permission_denied_view(request, exception=None):
    return render(request, "custom_error_page/403.html", {})


def custom_bad_request_view(request, exception=None):
    return render(request, "custom_error_page/400.html", {})


def testapi(request):
    return render(request, "testapi.html")


def hx_get_search_list(request):
    q = request.GET.get("q")
    movie_list = [
        {
            "title": item.title,
            "model": item.get_model_name,
            "slug": item.slug,
            "tmdb_thumbnail": item.tmdb_thumbnail,
            "type": item.type,
        }
        for item in MovieModel.objects.filter(title__icontains=q)[:10]
    ]
    series_list = [
        {
            "title": item.title,
            "model": item.get_model_name,
            "slug": item.slug,
            "tmdb_thumbnail": item.tmdb_thumbnail,
            "type": item.type,
        }
        for item in SeriesModel.objects.filter(title__icontains=q)
    ]
    context = {
        "movie_list": movie_list,
        "series_list": series_list,
        # 'softgameobjs':softgameobjs,
    }

    return render(request, "app_main/partials/search_list.html", context)
