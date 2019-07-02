from django.contrib import admin
from apps.datos.models import DatoUsua,Habilidades,Logros,Educacion,Experiencia,Cargo

# Register your models here.

class DatoUsuaModelAdmin(admin.ModelAdmin):
    list_display = ['PerfProf']
    list_display_links = ['PerfProf']
    list_filter = ['PerfProf']

    class Meta:
        model = DatoUsua

admin.site.register(DatoUsua,DatoUsuaModelAdmin)

class HabilidadesModelAdmin(admin.ModelAdmin):
    list_display = ['NombHabi']
    list_display_links = ['NombHabi']
    list_filter = ['NombHabi']

    class Meta:
        model = Habilidades

admin.site.register(Habilidades,HabilidadesModelAdmin)

class LogrosModelAdmin(admin.ModelAdmin):
    list_display = ['NombLogr']
    list_display_links = ['NombLogr']
    list_filter = ['NombLogr']

    class Meta:
        model = Logros

admin.site.register(Logros,LogrosModelAdmin) 

class EducacionModelAdmin(admin.ModelAdmin):
    list_display = ['Titulo']
    list_display_links = ['Titulo']
    list_filter = ['Titulo']

    class Meta:
        model = Educacion

admin.site.register(Educacion,EducacionModelAdmin)

class ExperienciaModelAdmin(admin.ModelAdmin):
    list_display = ['Empresa']
    list_display_links = ['Empresa']
    list_filter = ['Empresa']

    class Meta:
        model = Experiencia

admin.site.register(Experiencia,ExperienciaModelAdmin) 

class CargoModelAdmin(admin.ModelAdmin):
    list_display = ['NombCarg']
    list_display_links = ['NombCarg']
    list_filter = ['NombCarg']

    class Meta:
        model = Cargo

admin.site.register(Cargo,CargoModelAdmin) 
