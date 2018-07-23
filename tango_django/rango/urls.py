from django.urls import path
from django.conf.urls import url
#from django.conf.urls import patterns
from . import views
from rango.views import add_category
from django.conf.urls import url
#from django.views.decocrators.csrf import csrf_exempt

urlpatterns = [
    path('',views.index,name='index'),
    path('/about',views.about,name="about"),
    path('/category/<category_name_url>',views.category,name = "category"),
]