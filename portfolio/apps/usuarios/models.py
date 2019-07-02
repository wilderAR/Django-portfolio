from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

#clase usuario
class Usuario(models.Model):
    NombUsua = models.CharField(max_length=255, default="", verbose_name = "Nombre Usuario")
    ApelUsua = models.CharField(max_length=255, default="", verbose_name = "Apellido Usuario")
    EmaiUsua = models.CharField(max_length=255, default="", verbose_name = "Correo Usuario")
    PassUsua = models.CharField(max_length=255, default="", verbose_name = "Contraseña usuario")
    EstaUsua = models.CharField(max_length=50, default="", verbose_name = "Estado")

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
    
    def __str__(self):
        return self.NombUsua
