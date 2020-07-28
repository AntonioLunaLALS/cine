from django.contrib import admin
from .models import Pelicula, Genero

# Register your models here.
class PeliculaAdmin(admin.ModelAdmin):
    list_display =['nombre', 'duracion', 'fecha']
    search_fields =['nombre', 'fecha']
    list_filter =['Genero']

admin.site.register(Pelicula, PeliculaAdmin)
admin.site.register(Genero)
