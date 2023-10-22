from django.urls import path

from . import views

urlpatterns = [
    # assign views.index to the URL
    path('', views.index, name='index'),
]
