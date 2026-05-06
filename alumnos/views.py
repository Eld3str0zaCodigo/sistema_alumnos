from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Carrera, Alumno

# --- VISTA DE INICIO ---
def index(request):
    return render(request, 'index.html')

# --- VISTAS PARA CARRERAS ---
class CarreraListView(ListView):
    model = Carrera
    template_name = 'carreras/listar.html'
    context_object_name = 'carreras'
    # Ordenamos para evitar errores de paginación en algunos motores SQL
    ordering = ['id'] 

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

# --- VISTAS PARA ALUMNOS ---
class AlumnoListView(ListView):
    model = Alumno
    template_name = 'alumnos/listar.html'
    context_object_name = 'alumnos'
    ordering = ['id']

class AlumnoCreateView(CreateView):
    model = Alumno
    template_name = 'alumnos/form.html'
    # IMPORTANTE: Asegúrate de que estos nombres coincidan con los de tu models.py
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