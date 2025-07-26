from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class UsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)
    nivel = forms.ChoiceField(choices=Usuario.NIVEL_CHOICES, required=True)

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'nivel', 'password1', 'password2']

class EditarUsuarioForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['readonly'] = True

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'nivel']
