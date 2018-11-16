from django.conf.urls import url, include
from rest_framework import routers
from home import views

router = routers.DefaultRouter()
router.register(r'messages', views.MessageViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^',include('dashboard.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('burst/', include('predictor.urls')),
    url('live/', include('live.urls')),
    url('mapbox/', include('mapbox.urls')),
    url('files/', include('files.urls')),
    url('landing/', include('landing.urls')),
]
