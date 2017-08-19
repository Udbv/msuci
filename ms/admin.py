from django.contrib import admin
from .models import *
admin.autodiscover()
# Register your models here.
admin.site.register(Singer)
admin.site.register(Genre)
admin.site.register(Album)
admin.site.register(Track)

class ReInLIne(admin.StackedInline):
    model = Singer

class SingerAdmin(admin.ModelAdmin):
    inlines = [
        ReInLIne,

    ]
