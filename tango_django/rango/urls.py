from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('/about',views.about,name="about"),
    path('/category/<category_name_url>',views.category,name = "category"),
    path('/rango/add_category/',views.add_category, name='add_category'),
]