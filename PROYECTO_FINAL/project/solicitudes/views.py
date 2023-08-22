from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect

from .models import Solicitudes
from .forms import SolicitudForm


def inicio(request):
    return render(request, 'pruebas.html')

class Inicio(View):

    template_name= 'pruebas.html'

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
