from django.contrib import admin
from django.urls import path,include

handler404 = 'app_main.views.custom_page_not_found_view'
handler500 = 'app_main.views.custom_error_view'
handler403 = 'app_main.views.custom_permission_denied_view'
handler400 = 'app_main.views.custom_bad_request_view'


urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path('nested_admin/', include('nested_admin.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('', include('app_main.urls')),
]
