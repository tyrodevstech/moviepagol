from django.urls import path
from . import views

urlpatterns = [
    path('get_search_content', views.getSearchContent,name='getSearchContent'),
    path('getSearchTMDBMoviesData', views.getSearchTMDBMoviesData,name='getSearchTMDBMoviesData'),
    path('getSearchTMDBSeriesData', views.getSearchTMDBSeriesData,name='getSearchTMDBSeriesData'),
    path('getSeasonModelData/<int:seasonId>', views.getSeasonModelData,name='getSeasonModelData'),
]