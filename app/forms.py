from django import forms
from django.forms.fields import CharField


class ContatoForm(forms.Form):
    titulo = forms.CharField(label='', max_length=100, widget=forms.TextInput(
        attrs={
            'placeholder': 'Título do email',
            'class': 'form-control'
        }
    ))
    corpo = forms.CharField(label='',widget=forms.Textarea(
        attrs={
            'placeholder': 'Corpo do email', 
            'rows': '5',
            'class': 'form-control',
            'id':'exampleFormControlTextarea1'
        }
    ))
