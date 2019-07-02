from django.contrib import admin 
from apps.usuarios.models import Usuario

# Register your models here.

class UsuarioModelAdmin(admin.ModelAdmin):
    list_display = ['NombUsua']
    list_display_links = ['NombUsua']
    list_filter = ['NombUsua']

    class Meta:
        model = Usuario

admin.site.register(Usuario,UsuarioModelAdmin)
