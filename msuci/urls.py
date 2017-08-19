"""msuci URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from ms import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.IndexView.as_view(),name='index'),
    url(r'^singer/$', views.SingerView.as_view(), name='singer'),
    url(r'^singer/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='singer_detail'),
    url(r'^album/$', views.AlbumView.as_view(), name='album'),
    url(r'^album/(?P<pk>[0-9]+)/$', views.AlbumDetailView.as_view(), name='album_detail'),
    url(r'^genre/$', views.GenreView.as_view(), name='genre'),


]