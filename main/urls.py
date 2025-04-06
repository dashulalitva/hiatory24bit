from tkinter.font import names
from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index, name='timeline'),
    path('test/', views.test_view, name='test_view'),
    path('map/', views.map_interactive, name='map_interactive'),
]