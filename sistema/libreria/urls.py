
from django.contrib import admin
from django.urls import path
from. import views
from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros/', views.nosotros, name='nosotros'),#libreria/nosotoros
    path('libros/', views.libros, name='libros'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('crear/', views.crear, name='crear'),
    path('eliminar/<int:id>',views.eliminar, name='eliminar'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

