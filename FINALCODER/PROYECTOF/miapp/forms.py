from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from miapp.models import Jugadores



class UserRegisterForm(UserCreationForm):
    usuario = forms.CharField(label="usuario")
    password1 = forms.CharField(label="contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="repetir la contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
        help_text = {k:"" for k in fields}
    

class UserEditForm(UserCreationForm):
    usuario = forms.CharField(label="Modificar usuario")
    password1 = forms.CharField(label="contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="repetir la contraseña", widget=forms.PasswordInput)
    
    class meta:
        model = User
        fields = [ "nombre", "password1", "password"]
        help_text = {k:"" for k in fields}
        

class FormularioEditar(forms.ModelForm):
    class Meta:
        model = Jugadores
        fields = ['nombre', 'edad', 'nacionalidad', 'ultimo_equipo', 'nuevo_equipo', 'valor_de_traspaso']
