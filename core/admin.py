from django.contrib import admin
from core.models import Evento

class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_criacao', 'data_evento')
    list_filter = ('titulo','data_evento',)

admin.site.register(Evento, EventoAdmin)


