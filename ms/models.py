from django.db import models


# Create your models here.
class Genre(models.Model):
    genre_name = models.CharField(max_length=20)
    genre_album = models.CharField(max_length=20)
    def __str__(self):
        return self.genre_name




class Track(models.Model):
    track_name = models.CharField(max_length=200)
    track_album = models.CharField(max_length=200)

    def __str__(self):
        return "%s %s " %(self.track_name,self.track_album)


class Singer(models.Model):
    singer_first_name = models.CharField(max_length=50)
    singer_last_name = models.CharField(max_length=200)
    album_name = models.CharField(max_length=200)

    def __str__(self):

        return " %s Исполнитель %s %s"%(self.id,self.singer_last_name,self.album_name)


class Album(models.Model):

    album_name = models.CharField(max_length=200)
    album_singer =models.ForeignKey(Singer,on_delete=models.CASCADE,related_name='al_sing')
    album_track = models.ForeignKey(Track)
    album_genre = models.ForeignKey(Genre)

    def __str__(self):
        return " %s %s %s "%(self.album_name,self.album_singer,self.album_track)


