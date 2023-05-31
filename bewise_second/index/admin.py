from django.contrib import admin
from .models import Audio, Person


class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'token')
    list_display_links = ('name',)
    search_fields = ('name', 'id')


class AudioAdmin(admin.ModelAdmin):
    list_display = ('id', 'audio', 'audio_token', 'person')
    list_display_links = ('id',)
    search_fields = ('id', 'person')
    list_filter = ('person',)


admin.site.register(Person, PersonAdmin)
admin.site.register(Audio, AudioAdmin)
