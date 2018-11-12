from django.urls import path

from . import views

urlpatterns = [
    path('predictor/', views.index, name='index'),
]