from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('movies/<str:type>', views.movies_view,name='movies'),
    path('series/<str:type>', views.series_view,name='series'),
    path('softwaresgames/<str:category>', views.softwaresGames_view,name='softwaresGames'),
    path('genres/<str:genrename>', views.genres_view,name='genres'),
    path('classic/<str:type>', views.classic_view,name='classic'),

    path('director/<str:directorName>', views.director_contents_view,name='director_contents'),
    path('actor/<str:actorName>', views.actor_contents_view,name='actor_contents'),
    path('writer/<str:writerName>', views.writer_contents_view,name='writer_contents'),
    path('bsubcreator/<str:creatorSlug>', views.bsubcreator_contents_view,name='bsubcreator_contents'),

    path('dualaudio', views.dualaudio_view,name='dualaudio'),
    path('bsub', views.bsub_view,name='bsub'),
    path('hindidubbed', views.hindidubbed_view,name='hindidubbed'),
    path('satyajitray', views.satyajitray_view,name='satyajitray'),
    path('jamesbond', views.jamesbond_view,name='jamesbond'),
    path('imdbtop', views.imdbtop_view,name='imdbtop'),
    path('oscarwinning', views.oscarwinning_view,name='oscarwinning'),
    path('superhero', views.superhero_view,name='superhero'),
    path('found_footage', views.foundFootage_view,name='found_footage'),

    path('details/movie/<slug:pk>', views.details_movie_view,name='details_movie'),
    path('details/series/<slug:pk>', views.details_series_view,name='details_series'),
    path('details/<str:category>/<slug:pk>', views.details_softwaresGames_view,name='details_softwaresGames'),
    path('details/series/season/<int:pk>', views.details_season_view,name='details_season'),

    path('search', views.search_view,name='search'),
    path('contactus', views.contactus_view,name='contactus'),
    path('aboutus', views.aboutus_view,name='aboutus'),
    path('privacy', views.privacy_view,name='privacy'),
    path('index', views.fileserver_view,name='fileserver'),
    path('hx-search-list', views.hx_get_search_list,name='hx_search_list'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
