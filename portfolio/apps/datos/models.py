from django.db import models
from ckeditor.fields import RichTextField
from apps.parametros.models import Etnia,TipoDocu,EstaCivi,TipoLogr,TipoEduc,Pais,Departamento,Ciudad
from apps.usuarios.models import Usuario
# Create your models here.

#clase cargo
class Cargo(models.Model):

    NombCarg = models.CharField(max_length=750, default="", verbose_name="Nombre Cargo")

    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"

    def __str__(self):
        return self.NombCarg

#clase datos de usuario
class DatosUsua(models.Model):
    
    IdUsuarios = models.ForeignKey(Usuario,on_delete = models.CASCADE, verbose_name = "Numero Usuario")
    IdTipoDocu = models.ForeignKey(TipoDocu,on_delete = models.CASCADE, verbose_name = "Tipo Documento")
    IdEstaCivi = models.ForeignKey(EstaCivi,on_delete = models.CASCADE, verbose_name = "Estado Civil")
    IdEtnias = models.ForeignKey(Etnia,on_delete = models.CASCADE, verbose_name = "Etnia")
    IdDepartamentos = models.ForeignKey(Departamento,on_delete = models.CASCADE, verbose_name = "Departamento")
    IdPaises = models.ForeignKey(Pais, on_delete = models.CASCADE, verbose_name = "Pais")
    PerfilPro = models.CharField(max_length=200, default="", verbose_name = "Perfil Profesional")
    Genero = models.CharField(max_length=45, default="", verbose_name = "Genero")
    Telefono = models.CharField(max_length=45, default="", verbose_name = "Telefono")
    Direccion = models.CharField(max_length=255, default="", verbose_name = "Direccion")

    class Meta: 
        verbose_name = "Datos Usuario"
        verbose_name_plural = "Datos Usuarios"
    
    def __str__(self):
        return self.PerfProf

#clase habilidades
class Habilidad(models.Model):

    IdUsuarios = models.ForeignKey(Usuario,on_delete = models.CASCADE, verbose_name = "Numero Usuario")
    NombHabil = models.CharField(max_length=155, default="", verbose_name = "Nombre Habilidad")
    NiveHabil = models.CharField(max_length=50, default="", verbose_name = "Nivel Habilidad")

    class Meta:
        verbose_name = "Habilidad"
        verbose_name_plural = "Habilidades"
    
    def __str__(self):
        return self.NombHabi

#clase Logros
class Logro(models.Model):

    IdTipoLogr = models.ForeignKey(TipoLogr,on_delete=models.CASCADE, verbose_name = "Tipo de logro")
    IdUsuarios = models.ForeignKey(Usuario,on_delete=models.CASCADE, verbose_name = "Usuario")
    FechLogr = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name="Fecha de Logro")
    NombLogr = models.CharField(max_length=100, default="", verbose_name="Nombre de Logro")
    DescLogr = models.CharField(max_length=750, default="", verbose_name="Descripcion Logro") 

    class Meta:
        verbose_name = "Logro"
        verbose_name_plural = "Logros"

    def __str__(self):
        return self.NombLogr

#clase educacion
class Educacion(models.Model):
    
    IdTipoEstu = models.ForeignKey(TipoEduc,on_delete=models.CASCADE, verbose_name = "Tipo de Educación") 
    IdUsuarios = models.ForeignKey(Usuario,on_delete=models.CASCADE, verbose_name = "Usuario")
    IdCiudades = models.ForeignKey(Ciudad,on_delete=models.CASCADE, verbose_name = "Ciudad")
    IdDepartamentos = models.ForeignKey(Departamento,on_delete=models.CASCADE, verbose_name = "Departamento")
    IdPaises = models.ForeignKey(Pais,on_delete=models.CASCADE, verbose_name = "Pais")
    Instituto = models.CharField(max_length=155, default="", verbose_name = "Instituto")
    Titulo = models.CharField(max_length=155, default="", verbose_name = "Titulo")
    FechGrado = models.DateTimeField(auto_now = False, verbose_name = "Fecha de Grado")

    class Meta: 
        verbose_name = "educacion"
        verbose_name_plural = "educaciones"

    def __str__(self):
        return self.Titulo   

#clase experiencia
class Experiencia(models.Model):

    IdUsuarios = models.ForeignKey(Usuario,on_delete=models.CASCADE, verbose_name = "Usuario")
    IdCargo = models.ForeignKey(Cargo,on_delete=models.CASCADE, verbose_name = "Cargo")
    IdCiudad = models.ForeignKey(Ciudad,on_delete=models.CASCADE, verbose_name = "Ciudad")
    IdDepartamentos = models.ForeignKey(Departamento,on_delete=models.CASCADE, verbose_name = "Departamento")
    IdPaises = models.ForeignKey(Pais,on_delete=models.CASCADE, verbose_name = "Pais")
    Empresa = models.CharField(max_length=225, default="", verbose_name="Empresa")
    FechaInic = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name="Fecha de Inicio") 
    FechaFin = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name="Fecha de Finalizacion")
    Funciones = models.CharField(max_length=500, default="", verbose_name="Funciones") 
    Logros = models.CharField(max_length=500, default="", verbose_name="Logros") 

    class Meta:
        verbose_name = "Experiencia"
        verbose_name_plural = "Experiencias"

    def __str__(self):
        return self.Empresa