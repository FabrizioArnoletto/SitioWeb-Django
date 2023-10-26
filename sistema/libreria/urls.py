
from django.contrib import admin
from django.urls import path
from. import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros/', views.nosotros, name='nosotros'),#libreria/nosotoros
    path('libros/', views.libros, name='libros'),
    path('form/', views.librosf, name='form'),
    path('editar/', views.librose, name='editar'),
    path('crear/', views.librosc, name='crear'),
    path('signup/', views.sesion, name='sesion'),
    path('eliminar/<int:id>',views.librose, name='eliminar')
]

