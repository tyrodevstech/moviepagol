from django.contrib import admin
from .models import BsubCreatorModel, GenreModel, LinkEpisodeCategory, LinkEpisodeSource, LinkEpisodeSubCategory, MovieModel, Notice,SeriesModel,SeasonModel,EpisodeModel,SoftwaresGamesModel, SpecialModel, TopSlideModel , BSubModel,ClassicModel,DualAudioModel,SatyajitRayModel,FootageModel, JamesBondModel,HindiDubbedModel, IMDBTopModel,OscarWinningModel,SuperheroModel,LinkSource,LinkCategory,LinkSubCategory
from django_summernote.admin import SummernoteModelAdmin
import nested_admin
admin.site.site_header = 'Movie Pagol Administration'

# Register your models here.
admin.site.register(GenreModel)
admin.site.register(ClassicModel)
admin.site.register(HindiDubbedModel)
admin.site.register(SatyajitRayModel)
admin.site.register(JamesBondModel)
admin.site.register(IMDBTopModel)
admin.site.register(OscarWinningModel)
admin.site.register(FootageModel)
admin.site.register(SuperheroModel)
admin.site.register(BsubCreatorModel)
admin.site.register(LinkSource)
admin.site.register(LinkCategory)
admin.site.register(LinkSubCategory)
admin.site.register(LinkEpisodeSource)
admin.site.register(LinkEpisodeCategory)
admin.site.register(LinkEpisodeSubCategory)
admin.site.register(Notice)


class LinkSubCategoryInline(nested_admin.NestedStackedInline):
    model = LinkSubCategory
    extra = 0

class LinkCategoryInline(nested_admin.NestedStackedInline):
    model = LinkCategory
    inlines = [LinkSubCategoryInline]
    extra = 0

class LinkSourceInline(nested_admin.NestedStackedInline):
    model = LinkSource
    inlines = [LinkCategoryInline]
    extra = 0


class MovieModelAdmin(SummernoteModelAdmin,nested_admin.NestedModelAdmin):
    list_display=('title','type','release_date','created_at')
    list_filter=('type','genre','release_date')
    search_fields = ['title','release_date']
    ordering = ['-created_at']
    add_form_template = 'custom_add_form/movie_add_form.html'
    change_form_template = 'custom_add_form/movie_add_form.html'
    summernote_fields = ('synopsys',)

    inlines = [
        LinkSourceInline,
    ]

    def save_model(self, request, obj, form, change):

      if not obj.last_update:
        obj.update(request)
      elif form.changed_data:
        obj.update(request)

      obj.create(request)
      super(MovieModelAdmin, self).save_model(request, obj, form, change)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser

        if not is_superuser:
            form.base_fields['created_by'].disabled = True
            form.base_fields['last_update'].disabled = True
        return form
admin.site.register(MovieModel,MovieModelAdmin)


class BSubModelAdmin(admin.ModelAdmin):
  list_filter=('movie_content__type','movie_content__genre',)
  search_fields = ['movie_content__title','movie_content__release_date']
admin.site.register(BSubModel,BSubModelAdmin)


class DualAudioModelAdmin(admin.ModelAdmin):
  list_filter=('movie_content__type','movie_content__genre',)
  search_fields = ['movie_content__title','movie_content__release_date']
admin.site.register(DualAudioModel,DualAudioModelAdmin)


class SeriesModelAdmin(SummernoteModelAdmin):
    list_display=('title','type','rating','release_date','created_at')
    list_filter=('type','genre','release_date')
    search_fields = ['title','release_date']
    ordering = ['-created_at']
    add_form_template = 'custom_add_form/series_add_form.html'
    change_form_template = 'custom_add_form/series_add_form.html'
    summernote_fields = ('synopsys',)
    def save_model(self, request, obj, form, change):
      if not obj.last_update:
        obj.update(request)
      elif form.changed_data:
        obj.update(request)

      obj.create(request)
      super(SeriesModelAdmin, self).save_model(request, obj, form, change)
admin.site.register(SeriesModel,SeriesModelAdmin)


class SeasonModelAdmin(admin.ModelAdmin):
    @admin.display(description='Series')
    def series_title(self, obj):
      return f'{obj.series.title}'
    list_display=('series_title','season_number','episode_count','release_date','created_at')
    list_filter=('season_number','release_date')
    ordering = ['-created_at']
    search_fields = ['series__title','release_date',]
    # def get_search_results(self, request, queryset, search_term):
    #     queryset, use_distinct = super(SeasonModelAdmin, self).get_search_results(request, queryset, search_term)
    #     search_term_list = list(filter(None,search_term.split(' ')))
    #     print(search_term_list)
    #     # query_condition = ''
    #     # if search_term_list:
    #     #   search_columns = ('series__title__icontains',)
    #     #   query_condition = reduce(operator.or_, [Q(**{c:v}) for c in search_columns for v in search_term_list])
    #     #   print(query_condition)
    #     # queryset = self.model.objects.filter(query_condition)
    #     return queryset, use_distinct
admin.site.register(SeasonModel,SeasonModelAdmin)


class LinkEpisodeSubCategoryInline(nested_admin.NestedStackedInline):
    model = LinkEpisodeSubCategory
    extra = 0

class LinkEpisodeCategoryInline(nested_admin.NestedStackedInline):
    model = LinkEpisodeCategory
    inlines = [LinkEpisodeSubCategoryInline]
    extra = 0

class LinkEpisodeSourceInline(nested_admin.NestedStackedInline):
    model = LinkEpisodeSource
    inlines = [LinkEpisodeCategoryInline]
    extra = 0
class EpisodeModelAdmin(nested_admin.NestedModelAdmin):
    list_display=('season','title','episode','rating','created_at')
    list_filter=('season','episode')
    search_fields = ['season__series__title','title',]
    ordering = ['-created_at']
    add_form_template = 'custom_add_form/episode_add_form.html'
    change_form_template = 'custom_add_form/episode_add_form.html'
    inlines = [
        LinkEpisodeSourceInline,
    ]

admin.site.register(EpisodeModel,EpisodeModelAdmin)


class SoftwaresGamesModelAdmin(admin.ModelAdmin):
    list_display=('title','category','platform','size','release_date')
    list_filter=('category','platform')
    search_fields = ['title','release_date']
admin.site.register(SoftwaresGamesModel,SoftwaresGamesModelAdmin)


class TopSlideModelAdmin(admin.ModelAdmin):
  def has_add_permission(self, request):
    num_objects = self.model.objects.count()
    if num_objects >= 10:
      return False
    else:
      return True
admin.site.register(TopSlideModel, TopSlideModelAdmin)


class SpecialModelAdmin(admin.ModelAdmin):
  def has_add_permission(self, request):
    num_objects = self.model.objects.count()
    if num_objects >= 1:
      return False
    else:
      return True
admin.site.register(SpecialModel, SpecialModelAdmin)