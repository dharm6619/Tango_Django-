from django.urls import path
from django.conf.urls import url
from rango import views
urlpatterns = [
    
    path('',views.index, name = "index"),
    path('about', views.about, name='about'),
    
]
