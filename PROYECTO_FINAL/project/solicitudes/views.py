from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404

from .models import Solicitudes
from .forms import SolicitudForm


'''
def login(request):
    return render(request, 'login.html')
'''
'''def versolicitudes(request):
    return render(request, 'ver-solicitudes.html')
'''
'''
def crearsolicitud(request):
    return render(request, 'crear-solicitud.html')
'''
def base(request):
    return render(request, 'base.html')

def inicio(request):
    return render(request, 'index.html')


class Ver(View):
    teamplate_name= 'ver-solicitudes.html'
    def post(self, request):   
        return render(request, self.teamplate_name)
    
    def get(self, request):
        #con la sig linea mandamos a llamar a las solicitudes
        soli = Solicitudes.objects.all()
        return render(request, self.teamplate_name, {'soli' : soli})
    
class crear(View):
    teamplate_name = 'crear-solicitud.html'
    def post(self, request):
        form = SolicitudForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        
        return render(request, self.teamplate_name, {'form': form})
    def get(self, request):
      form = SolicitudForm()
      return render(request, self.teamplate_name, {'form': form})

class eliminarSolicitud(View):
    def post(self, request, solicitud_id):
        libro = get_object_or_404(Solicitudes, pk=solicitud_id)
        libro.delete()
        return redirect('ver')






'''def insertar_solicitud(request):
    nueva_solicitud = Solicitudes(
        titulo = 'Falta de alumbrado',
        descripcion = 'Falta de luz en mi colonia',
        fecha_de_registro = '2023-8-25',
        estatus = 'sin revisar'
    )
    nueva_solicitud.save()

    return HttpResponse('Solicitud insertada correctamente')
'''


'''    def post(self, request):
        form = SolicitudForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
        
        return render(request, self.template_name, {'form': form})
    
    def get(self, request):
        form = SolicitudForm()
        return render(request, self.template_name, {'form': form})
'''
