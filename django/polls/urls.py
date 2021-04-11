from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.Index, name='index'),
    path('url_shortener/', views.url_shortener, name='url_shortener'),
    path('<str:short>/redirect/', views.redirect, name='redirect'),
]
