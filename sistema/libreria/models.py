from django.db import models

class Libro(models.Model):
    ID=models.AutoField(primary_key=True)
    Titulo=models.CharField(max_length=100,verbose_name="Titulo")
    Imagen=models.ImageField(upload_to='imagenes/',verbose_name="Imagen",null=True)
    Descripcion=models.TextField(null=True,verbose_name="Descripción")

    def __str__(self):
        fila= "Titulo: " + self.Titulo + "-" + "Descripcion " + self.Descripcion
        return fila

    def delete(self, using=None, Keep_parents=False):
        self.Imagen.storage.delete(self.Imagen.name)
        super().delete()