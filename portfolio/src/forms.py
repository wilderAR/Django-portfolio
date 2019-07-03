from django import forms
from parametros.models import TipoDocu,EstaCivil,Etnia,Cargo,TipoEstu
from .models import Habilidad,DatosUsua,Experiencia,Educacion
from .choices import NivelHabilidad,GENEROS
from django.forms import formset_factory

class MultipleForm(forms.ModelForm):
    action = forms.CharField(max_length=60,widget=forms.HiddenInput())

    

class DatosPersonaForm(MultipleForm):
    IdTipoDocu = forms.ModelChoiceField(label="Tipo de documento",queryset=TipoDocu.objects.all(),required=True,widget=forms.Select(attrs={'class':'form-control'}),)
    IdUsuarios = forms.CharField(label="Numero de documento",widget=forms.TextInput(attrs={'class':'form-control'}),required=True)
    Genero = forms.ChoiceField(choices=GENEROS,label="Genero",required=True,widget=forms.Select(attrs={'class':'form-control'}),)
    IdEtnias = forms.ModelChoiceField(label="Etnia",queryset=Etnia.objects.all(),required=True,widget=forms.Select(attrs={'class':'form-control'}),)
    IdEstaCivil = forms.ModelChoiceField(label="Estado civil",queryset=EstaCivil.objects.all(),required=True,widget=forms.Select(attrs={'class':'form-control'}),)
    IdPaises = forms.CharField(label="País",widget=forms.TextInput(attrs={'class':'form-control'}),required=True)
    IdDepartamentos = forms.CharField(label="Departamento",widget=forms.TextInput(attrs={'class':'form-control'}),required=True)
    IdCiudades = forms.CharField(label="Ciudad",widget=forms.TextInput(attrs={'class':'form-control'}),required=True)
    Direccion = forms.CharField(label="Dirección",widget=forms.TextInput(attrs={'class':'form-control'}),required=True)
    Telefono = forms.CharField(label="Teléfono",widget=forms.TextInput(attrs={'class':'form-control'}),required=True)
    PerfilPro = forms.CharField(label="Perfil",required=True,widget=forms.Textarea(attrs={'class':'form-control','rows':'6','cols':'150'}))

    class Meta:
        model = DatosUsua
        fields = ('IdTipoDocu','IdUsuarios','Genero','IdEtnias','IdEstaCivil','IdPaises','IdDepartamentos','IdCiudades','Direccion','Telefono','PerfilPro')

class ExperienciaForm(MultipleForm):
    IdUsuarios = forms.CharField(label="Numero de documento",widget=forms.TextInput(attrs={'class':'form-control'}),)
    IdCargos = forms.ModelChoiceField(label="Cargo", queryset=Cargo.objects.all(),required=True,widget=forms.Select(attrs={'class':'form-control'}),)
    IdPaises = forms.CharField(label="Numero del paises", widget=forms.TextInput(attrs={'class':'form-control'}),)
    IdDepartamentos = forms.CharField(label="Numero del departamento", widget=forms.TextInput(attrs={'class':'form-control'}),)
    IdCiudades = forms.CharField(label="Numero de ciudad", widget=forms.TextInput(attrs={'class':'form-control'}),)
    Empresa = forms.CharField(label="Nombre de la empresa", widget=forms.TextInput(attrs={'class':'form-control'}),)
    FechaIni = forms.DateField(label="Fecha inicial", widget=forms.DateInput(attrs={'class':'form-control'}),)
    FechaFin = forms.DateField(label="Fecha inicial", widget=forms.DateInput(attrs={'class':'form-control'}),)
    Funciones = forms.CharField(label="Nombre de la funcion", widget=forms.TextInput(attrs={'class':'form-control'}),)
    Logros = forms.CharField(label="Nombre del logro", widget=forms.TextInput(attrs={'class':'form-control'}),)
    
    class Meta:
        model = Experiencia
        fields = ('IdUsuarios','IdCargos','IdPaises','IdDepartamentos','IdCiudades','Empresa','FechaIni','FechaFin','Funciones','Logros')

ExperienciaFormSet = formset_factory(ExperienciaForm)

class EducacionesForm(MultipleForm):
    IdTipoEstu = forms.ModelChoiceField(label="TipoEstu", queryset=TipoEstu.objects.all(),required=True,widget=forms.Select(attrs={'class':'form-control'}),)
    IdUsuarios = forms.CharField(label="Usuario",widget=forms.TextInput(attrs={'class':'form-control'}),)
    IdPaises = forms.CharField(label="Pais",widget=forms.TextInput(attrs={'class':'form-control'}),)
    IdDepartamentos = forms.CharField(label="Departamento",widget=forms.TextInput(attrs={'class':'form-control'}),)
    IdCiudades = forms.CharField(label="Ciudad",widget=forms.TextInput(attrs={'class':'form-control'}),)
    Instituto = forms.CharField(label="Institución",widget=forms.TextInput(attrs={'class':'form-control'}),)
    Titulo = forms.CharField(label="Titulo",widget=forms.TextInput(attrs={'class':'form-control'}),)
    FechGrado = forms.DateField(label="Fecha grado", widget=forms.DateInput(attrs={'class':'form-control'}),)
    class Meta:
        model = Educacion
        fields = ('IdTipoEstu','IdUsuarios','IdPaises','IdDepartamentos','IdCiudades','Instituto','Titulo','FechGrado')

EducacionesFormSet = formset_factory(EducacionesForm)

class HabilidadForm(MultipleForm):
    IdUsuarios = forms.CharField(label="Usuario",widget=forms.TextInput(attrs={'class':'form-control'}),)
    NombHabil = forms.CharField(label="Nombre",widget=forms.TextInput(attrs={'class':'form-control'}),)
    NiveHabil = forms.ChoiceField(choices=NivelHabilidad,label="Nivel",required=True,widget=forms.Select(attrs={'class':'form-control'}),)
    class Meta:
        model = Habilidad
        fields = ('IdUsuarios', 'NombHabil' ,'NiveHabil')

HabilidadFormSet = formset_factory(HabilidadForm)