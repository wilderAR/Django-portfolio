from django.contrib import admin
from apps.parametros.models import Etnia,TipoDocu,EstaCivi,TipoLogr,TipoEduc,Pais,Departamento,Ciudad

# Register your models here.
class EtniaModelAdmin(admin.ModelAdmin):
    list_display = ['NombEtni']
    list_display_links = ['NombEtni']
    list_filter = ['NombEtni']

    class Meta:
        model = Etnia

admin.site.register(Etnia,EtniaModelAdmin)


class TipoDocuModelAdmin(admin.ModelAdmin):
    list_display = ['NombTipoDocu']
    list_display_links = ['NombTipoDocu']
    list_filter = ['NombTipoDocu']

    class Meta:
        model = TipoDocu

admin.site.register(TipoDocu,TipoDocuModelAdmin)

class EstaCiviModelAdmin(admin.ModelAdmin):
    list_display = ['NombEstaCivi']
    list_display_links = ['NombEstaCivi']
    list_filter = ['NombEstaCivi']

    class Meta:
        model = EstaCivi

admin.site.register(EstaCivi,EstaCiviModelAdmin)

class TipoLogrModelAdmin(admin.ModelAdmin):
    list_display = ['NombTipoLogr']
    list_display_links = ['NombTipoLogr']
    list_filter = ['NombTipoLogr']
    
    class Meta:
        model = TipoLogr

admin.site.register(TipoLogr,TipoLogrModelAdmin)

class TipoEducModelAdmin(admin.ModelAdmin):
    list_display = ['NombTipoEduc']
    list_display_links = ['NombTipoEduc']
    list_filter = ['NombTipoEduc']
    class Meta:
        model = TipoEduc

admin.site.register(TipoEduc,TipoEducModelAdmin)

class PaisModelAdmin(admin.ModelAdmin):
    list_display = ['NombPais']
    list_display_links = ['NombPais']
    list_filter = ['NombPais']

    class Meta:
        model = Pais

admin.site.register(Pais,PaisModelAdmin)

class DepartamentoModelAdmin(admin.ModelAdmin):
    list_display = ['NombDepa']
    list_display_links = ['NombDepa']
    list_filter = ['NombDepa']

    class Meta:
        model = Departamento

admin.site.register(Departamento,DepartamentoModelAdmin)

class CiudadModelAdmin(admin.ModelAdmin):
    list_display = ['NombCiud']
    list_display_links = ['NombCiud']
    list_filter = ['NombCiud']

    class Meta:
        model = Ciudad

admin.site.register(Ciudad,CiudadModelAdmin)