from django.db import models

class Libro(models.Model):
    ID=models.AutoField(primary_key=True)
    Titulo=models.CharField(max_length=100,verbose_name="Titulo")
    Imagen=models.ImageField(upload_to='imagenes/',verbose_name="Imagen",null=True)
    Descripcion=models.TextField(null=True,verbose_name="Descripción")
    Promo=models.BooleanField(null=True,verbose_name="Promo")

    def __str__(self):
        fila= " " + self.Titulo 
        return fila

    def delete(self, using=None, Keep_parents=False):
        self.Imagen.storage.delete(self.Imagen.name)
        super().delete()

class comentarios(models.Model):
    ID_c=models.AutoField(primary_key=True)
    ID=models.ForeignKey(Libro, on_delete=models.CASCADE)
    Comentario=models.TextField(null=True,verbose_name="Comentario")
    
    def __str__(self):
        fila= "ID_c-ID: " + self.ID_c + "-" + self.ID +"Comentario" + self.Comentario
        return fila