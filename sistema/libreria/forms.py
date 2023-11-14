from django import forms
from .models import Libro, comentarios
class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'  

class comentariosForm(forms.ModelForm):
    class Meta:
        model = comentarios
        fields = '__all__'  