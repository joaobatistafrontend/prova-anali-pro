from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ArtModel

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Obrigatório. Digite um endereço de e-mail válido.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
class ArtForm(forms.ModelForm):
    class Meta:
        model = ArtModel
        fields = ['participacao', 'motivos', 'dados_contratante', 'anexos', 'normas_compliance']