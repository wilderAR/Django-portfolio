from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import DatosUsua,Habilidad,Experiencia,Educacion,Logro
from django.views.generic import CreateView,TemplateView,FormView
from django.urls import reverse_lazy, reverse
from .forms import DatosPersonaForm,ExperienciaForm,HabilidadForm,ExperienciaFormSet,HabilidadFormSet,EducacionesFormSet
from .multiforms import MultiFormsView
# Create your views here.

class PerfilListView(TemplateView):
    template_name = "perfil.html"

    def get_context_data(self, **kwargs):
        context = super(PerfilListView,self).get_context_data(**kwargs)
        context["datosusuario"] = DatosUsua.objects.filter(IdUsuarios="1")
        context["educaciones"] = Educacion.objects.filter(IdUsuarios="1")
        context["experiencias"] = Experiencia.objects.filter(IdUsuarios = "1")
        context["habilidades"] = Habilidad.objects.filter(IdUsuarios="1")
        context["logros"] = Logro.objects.filter(IdUsuarios="1")
        return context

class PerfilMultipleFormsView(MultiFormsView):
    template_name = "editar_perfil.html"
    form_classes = {'datospersona' : DatosPersonaForm,
                    'experienciasForm': ExperienciaFormSet,
                    'habilidadForm' : HabilidadFormSet,
                    'educacionForm' : EducacionFormSet
    }

    success_urls = {'datospersona': 'update?Id=1',
                    'experienciasForm' : 'update?Id=1'
    }
    

    def formularios_validar(self,form):
        if form.is_valid():
            form.save()
        return HttpResponseRedirect("update?Id=1")

    def datospersona_form_valid(self,form):
        form_name = form.cleaned_data.get('action')
        form.save()
        return HttpResponseRedirect('update?Id=1')

    def experienciasForm_form_valid(self,request,form_IdUser):
        datos = get_object_or_404(DatosUsua,pk=form_IdUser)
        if request.method == 'POST':
            formPersonas = DatosPersonaForm(request.POST,instance=datos)
            formset = ExperienciaFormSet(request.POST,prefix='experiencias')
            formsetHabilidad = HabilidadFormSet(request.POST,prefix='habilidades')
            formsetEducacion = EducacionFormSet(request.POST,prefix="educaciones")
            print(formsetEducacion)
            if formPersonas.is_valid() and formset.is_valid() and formsetHabilidad.is_valid():
                formPersonas.save()

                cont = 0
                for form in formset:
                    num = str(cont)
                    idForm = request.POST.get("experiencias-"+ num +"-id")
                    #print(dato)
                    delete = request.POST.get("experiencias-"+ num +"-DELETE")
                    print(delete)
                    if delete == 'on':
                        instance = Experiencia.objects.get(pk=idForm)
                        instance.delete()
                    else:
                        form.save()
                    cont = cont + 1

                cont = 0
                for form in formsetHabilidad:
                    num = str(cont)
                    idForm = request.POST.get("habilidades-"+ num +"-id")
                    
                    #print(dato)
                    delete = request.POST.get("habilidades-"+ num +"-DELETE")
                    print(delete)
                    if delete == 'on':
                        instance = Habilidad.objects.get(pk=idForm)
                        instance.delete()
                    else:
                        form.save()
                    cont = cont + 1
                cont = 0
                for form in formsetEducacion:
                    num = str(cont)
                    idForm = request.POST.get("educaciones-"+ num +"-id")
                    
                    #print(dato)
                    delete = request.POST.get("educaciones-"+ num +"-DELETE")
                    print(delete)
                    if delete == 'on':
                        instance = Educacion.objects.get(pk=idForm)
                        instance.delete()
                    else:
                        form.save()
                    cont = cont + 1    

                return HttpResponseRedirect('update?Id=1')
            else:
                return HttpResponseRedirect('update?Id=4')

 

    def datosgenerales_form_valid(self,form):
        Direccion = form.cleaned_data.get('Direccion')
        form_name = form.cleaned_data.get('action')
        print(Direccion)
        return HttpResponseRedirect(self.get_success_url(form_name))

    def habilidadForm_form_valid(self,form):
        form_name = form.cleaned_data.get('action')
        form.save()
        return HttpResponseRedirect(self.get_success_url(form_name))


def perfil(request):
    return render(request,'perfil.html')


