from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

# clase etnia
class Etnia(models.Model):
    
    NombEtni = models.CharField(max_length=50, default="", verbose_name = "Nombre Etnia")

    class Meta:
        verbose_name = "Etnia"
        verbose_name_plural = "Etnias"
    
    # se retorna un valor 
    def __str__(self):
        return self.NombEtni

#clase tipo de documentos
class TipoDocu(models.Model):

    NombTipoDocu = models.CharField(max_length=50, default="", verbose_name = "Tipo Documento")

    class Meta:
        verbose_name = "Tipo Documento"
        verbose_name_plural = "Tipos de Documentos"
    
    def __str__(self):
        return self.NombTipoDocu

#clase estado civil
class EstaCivi(models.Model):

    NombEstaCivi= models.CharField(max_length =50, default="", verbose_name = "Estado Civil")

    class Meta:
        verbose_name = "Estado Civil"
        verbose_name_plural = "Estados Civiles"
    
    def __str__(self):
        return self.NombEstaCivi

#clase tipos de logro
class TipoLogr(models.Model):

    NombTipoLogr = models.CharField(max_length=50, default="", verbose_name = " Tipo Logro")

    class Meta:
        verbose_name = "Tipo Logro"
        verbose_name_plural = "Tipos de Logros"

    def __str__(self):
        return self.NombTipoLogr

#clase tipo de educacion
class TipoEduc(models.Model):

    NombTipoEduc = models.CharField(max_length=50, default="", verbose_name = "Tipo Estudio")

    class Meta:
        verbose_name = "Tipo Estudio"
        verbose_name_plural = "Tipos de Estudios"
    
    def __str__ (self):
        return self.NombTipoEduced

#clase pais
class Pais(models.Model):
    
    NombPais = models.CharField(max_length=155, default="", verbose_name = "Nombre Pais")

    class Meta: 
        verbose_name = "Pais"
        verbose_name_plural = "Paises"

    def __str__(self):
        return self.NombPais

#clase departamento
class Departamento(models.Model):

    id_Paises = models.ForeignKey(Pais,on_delete=models.CASCADE, verbose_name = "Pais")
    NombDepa = models.CharField(max_length=155, default="", verbose_name = "Nombre de Departamento")

    class Meta: 
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"

    def __str__(self):
        return self.NombDepa

#clase ciudad
class Ciudad(models.Model):
    id_Departamentos = models.ForeignKey(Departamento,on_delete=models.CASCADE, verbose_name = "Departamento")
    id_Paises = models.ForeignKey(Pais,on_delete = models.CASCADE, verbose_name = "Pais")
    NombCiud = models.CharField(max_length=155, default="", verbose_name = "Nombre Ciudad")

    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"

    def __str__(self):
        return self.NombCiud