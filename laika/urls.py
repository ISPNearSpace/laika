from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('dashboard.urls')),
    path('predictor/', include('predictor.urls')),
    path('live/', include('live.urls')),
    path('mapbox/', include('mapbox.urls')),
    path('files/', include('files.urls')),
    path('burst/', include('burst.urls')),
    path('landing/', include('landing.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)