
from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros/', views.nosotros, name='nosotros'),#libreria/nosotoros
    path('libros/', views.libros, name='libros'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('crear/', views.crear, name='crear'),
    path('eliminar/<int:id>',views.eliminar, name='eliminar'),
    path('comentar/<int:id>',views.comentar, name='comentar'),
    path('com/<int:id>',views.com, name='com'),
    path('eliminarc/<int:id>',views.eliminarc, name='eliminarc'),
    path('editarc/<int:id>', views.editarc, name='editarc'),
]
