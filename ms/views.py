from django.views import generic
from .models import Singer,Track,Album,Genre

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'base_site'


    def get_queryset(self):
        """Return the last five published questions."""
        return Singer.objects.all()


#Сторінка пацієнта,має бути вся інфа

class SingerView(generic.ListView):
    template_name = 'singer.html'
    context_object_name = 'singer_list'
    model = Singer
    def get_queryset(self):
        """Return the last five published questions."""
        return Singer.objects.all()

class DetailView(generic.DetailView):
    model = Singer
    template_name = 'singer_detail.html'

#Журнал виїздів швидкої допомоги.Має бути видно


class AlbumView(generic.ListView):



    template_name = 'albums.html'
    context_object_name = 'album_list'
    model = Album
    def get_queryset(self):
        """Return the last five published questions."""
        return Album.objects.order_by('album_singer_id')[:6]

class AlbumDetailView(generic.DetailView):
    model = Album
    template_name = 'album_detail.html'


class GenreView(generic.ListView):
    model = Genre

    template_name = 'genre.html'
    context_object_name = 'genre_list'


