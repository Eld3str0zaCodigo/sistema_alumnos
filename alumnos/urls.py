from django.urls import path
from .views import (
    index,
    CarreraListView, CarreraCreateView, CarreraUpdateView, CarreraDeleteView,
    AlumnoListView, AlumnoCreateView, AlumnoUpdateView, AlumnoDeleteView
)

urlpatterns = [
    path('', index, name='index'),
    path('carreras/', CarreraListView.as_view(), name='carrera_list'),
    path('carreras/crear/', CarreraCreateView.as_view(), name='carrera_create'),
    path('carreras/<int:pk>/editar/', CarreraUpdateView.as_view(), name='carrera_update'),
    path('carreras/<int:pk>/eliminar/', CarreraDeleteView.as_view(), name='carrera_delete'),
    path('alumnos/', AlumnoListView.as_view(), name='alumno_list'),
    path('alumnos/crear/', AlumnoCreateView.as_view(), name='alumno_create'),
    path('alumnos/<int:pk>/editar/', AlumnoUpdateView.as_view(), name='alumno_update'),
    path('alumnos/<int:pk>/eliminar/', AlumnoDeleteView.as_view(), name='alumno_delete'),
]