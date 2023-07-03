from django.core.management.base import BaseCommand, CommandError
from app_main.models import MovieModel,LinkEpisodeSubCategory, SeasonModel

class Command(BaseCommand):
    def handle(self, *args, **options):
        pass
        # movies_qs = MovieModel.objects.all()
        # for movie in movies_qs:
        #     print(movie)
        #     for source in movie.linksource.all():
        #         # print('\t',source)
        #         for cat in source.linkcat.all():
        #             # print('\t\t',cat)
        #             for subcat in cat.linksubcat.all():
        #                 print('\t\t\t',subcat,subcat.link)
        #                 # if 'bsmbd.xyz' in subcat.link:
        #                 #     changed_link = subcat.link.replace('bsmbd.xyz','link.searcheverything.net')
        #                 #     subcat.link = changed_link
        #                 #     subcat.save()
        #                 #     print('\t\t\t after changed:',subcat,subcat.link)

        # for season in SeasonModel.objects.all():
        #     if season.download_full_quality_480p and 'bsmbd.xyz' in season.download_full_quality_480p:
        #         changed_link = season.download_full_quality_480p.replace('bsmbd.xyz','link.searcheverything.net')
        #         season.download_full_quality_480p = changed_link

        #     if season.download_full_quality_720p and 'bsmbd.xyz' in season.download_full_quality_720p:
        #         changed_link = season.download_full_quality_720p.replace('bsmbd.xyz','link.searcheverything.net')
        #         season.download_full_quality_720p = changed_link

        #     if season.download_full_quality_1080p and 'bsmbd.xyz' in season.download_full_quality_1080p:
        #         changed_link = season.download_full_quality_1080p.replace('bsmbd.xyz','link.searcheverything.net')
        #         season.download_full_quality_1080p = changed_link

        #     if season.download_full_quality_2160p and ('bsmbd.xyz' in season.download_full_quality_2160p):
        #         changed_link = season.download_full_quality_2160p.replace('bsmbd.xyz','link.searcheverything.net')
        #         season.download_full_quality_2160p = changed_link

        #     if season.download_full_download_dual_audio and ('bsmbd.xyz' in season.download_full_download_dual_audio):
        #         changed_link = season.download_full_download_dual_audio.replace('bsmbd.xyz','link.searcheverything.net')
        #         season.download_full_download_dual_audio = changed_link

        #     if season.download_full_download_hindi_dubbed and ('bsmbd.xyz' in season.download_full_download_hindi_dubbed):
        #         changed_link = season.download_full_download_hindi_dubbed.replace('bsmbd.xyz','link.searcheverything.net')
        #         season.download_full_download_hindi_dubbed = changed_link

        #     season.save()


        # for ep in LinkEpisodeSubCategory.objects.all():
        #     if 'bsmbd.xyz' in ep.link:
        #         changed_link = ep.link.replace('bsmbd.xyz','link.searcheverything.net')
        #         ep.link = changed_link
        #         ep.save()