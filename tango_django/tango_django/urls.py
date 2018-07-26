"""tango_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls import url
from rango.views import add_category,add_page


urlpatterns = [
    path('admin/', admin.site.urls),
    path('rango',include('rango.urls')),
    path('rango/about',include('rango.urls')),
    url(r'^rango/add_category/',add_category),
    url(r'^category/(?P<category_name_url>\w+)/add_page/$', add_page, name='add_page'),
]
#if settings.DEBUG :
 #   urlpatterns += path('django.views.static',('/media/(?P<path>.*)','serve',{'document_root': settings.MEDIA_ROOT}), )
