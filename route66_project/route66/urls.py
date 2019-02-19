# programming the routes
from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('gogetthegood/', views.gogetthegood, name='hey'),
    path('happyhappyjoyjoy/', views.happyhappyjoyjoy, name='RAS'),
]