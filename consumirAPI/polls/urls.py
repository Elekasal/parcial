from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('organismos/', views.organismos, name="organismos"),
    path('programas/', views.programas, name="programas"),
    path('museos/', views.museos, name="museos"),
    path('institutos/', views.institutos, name="institutos"),
    path('tramites/', views.tramites, name="tramites"),
    path('convocatorias/', views.convocatorias, name="convocatorias")
]