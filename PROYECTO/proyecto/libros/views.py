from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Libros
from .forms import LibroForm
from django.db.models import Sum, Max, Avg

# Create your views here.
def index(request):
 return HttpResponse("Hola mundo")



class Inicio(View):
    template_name = 'inicio.html'

    def post(self, request):

        return render(request, self.template_name)
    
    @method_decorator(login_required)
    def get(self, request):
        libros = Libros.objects.all()

        return render(request, self.template_name, {'libros': libros})
    

class Formulario(View):
   template_name='formulario.html'

   def get(self, request):
      form = LibroForm(request.POST)
      if form.is_valid():
           form.save()
           return redirect('inicio')
      
      return render(request, self.template_name, {'form': form})
   
   @method_decorator(login_required) 
   def get(self, request):
      form = LibroForm()
      return render(request, self.template_name, {'form': form})

class EliminarLibro(View):
   def post(self, request, libro_id):
      libro = get_object_or_404(Libros, pk=libro_id)
      libro.delete()
      return redirect('inicio')
   
def estadisticas_libros(request):
    #Obtener el número total de páginas de todos los libros
    total_paginas = Libros.objects.aggregate(total_paginas = Sum('numero_paginas'))['total_paginas']

    #Obtener el año maxímo de publicación
    max_anio_publicación = Libros.objects.aggregate(max_anio_publicación = Max('año_publicacion'))['max_anio_publicación']

    #Obtener el promedio de paginas de todos los libros
    promedio_paginas = Libros.objects.aggregate(promedio_paginas = Avg('numero_paginas'))['promedio_paginas']

    return render(request, 'estadisticas/estadisticas_libros.html', {
    'total_paginas': total_paginas,
    'max_anio_publicación': max_anio_publicación, 'promedio_paginas':promedio_paginas})