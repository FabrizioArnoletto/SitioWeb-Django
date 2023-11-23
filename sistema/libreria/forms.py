from django import forms
from .models import Libro, Comentarios
class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'  

class comentariosForm(forms.ModelForm):
    class Meta:
        model = Comentarios
        fields = '__all__'  