from django.contrib import admin
from .models import Libro
# Register your models here.
admin.site.register(Libro)
def __str__(self):
    fila= "Titulo: " + self.titulo + "-" + "Descripcion " + self.descripcion
    return fila
def delete(self, using=None, Keep_parents=False):
    self.imagen.storage.delete(self.imagen.name)
    super(Libro).delete()