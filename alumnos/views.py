from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Carrera, Alumno

# Create your views here.

# Vistas para Carreras
class CarreraListView(ListView):
    model = Carrera
    template_name = 'carreras/listar.html'
    context_object_name = 'carreras'

class CarreraCreateView(CreateView):
    model = Carrera
    template_name = 'carreras/form.html'
    fields = ['nombre', 'duracion']
    success_url = reverse_lazy('carrera_list')

class CarreraUpdateView(UpdateView):
    model = Carrera
    template_name = 'carreras/form.html'
    fields = ['nombre', 'duracion']
    success_url = reverse_lazy('carrera_list')

class CarreraDeleteView(DeleteView):
    model = Carrera
    template_name = 'carreras/confirm_delete.html'
    success_url = reverse_lazy('carrera_list')

# Vistas para Alumnos
class AlumnoListView(ListView):
    model = Alumno
    template_name = 'alumnos/listar.html'
    context_object_name = 'alumnos'

class AlumnoCreateView(CreateView):
    model = Alumno
    template_name = 'alumnos/form.html'
    fields = ['nombres', 'apellidos', 'dni', 'foto', 'id_carrera']
    success_url = reverse_lazy('alumno_list')

class AlumnoUpdateView(UpdateView):
    model = Alumno
    template_name = 'alumnos/form.html'
    fields = ['nombres', 'apellidos', 'dni', 'foto', 'id_carrera']
    success_url = reverse_lazy('alumno_list')

class AlumnoDeleteView(DeleteView):
    model = Alumno
    template_name = 'alumnos/confirm_delete.html'
    success_url = reverse_lazy('alumno_list')

# Vista de inicio
def index(request):
    return render(request, 'index.html')
