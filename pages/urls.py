from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'), #1st parameter is the path, 2nd parameter is the metho associate and 3rd is the name
    path('about', views.about, name = 'about')
]
