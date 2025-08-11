from django import forms

class ContactoForm(forms.Form):
    nombre = forms.CharField(
        label='Nombre completo',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Tu nombre'
        })
    )

    email = forms.EmailField(
        label='Correo electrónico',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'tu@email.com'
        })
    )

    asunto = forms.CharField(
        label='Asunto',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '¿Sobre qué quieres hablar?'
        })
    )

    mensaje = forms.CharField(
        label='Mensaje',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 5,
            'placeholder': 'Escribe tu mensaje aquí...'
        })
    )

    acepto_privacidad = forms.BooleanField(
        label='Acepto la política de privacidad',
        required=True
    )
