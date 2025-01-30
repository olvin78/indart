from django import forms


from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        label="Nombre",
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'nombre',
            'placeholder': 'Nombre',
        })
    )
    company = forms.CharField(
        label="Empresa",
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'empresa',
            'placeholder': 'Empresa',
        })
    )
    email = forms.EmailField(
        label="Email",
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'id': 'email',
            'placeholder': 'Email',
        })
    )
    country = forms.CharField(
        label="País",
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'pais',
            'placeholder': 'Escribe tu país',
        })
    )
    prefix = forms.CharField(
        label="Prefijo",
        max_length=5,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'style': 'max-width: 60px; text-align: center;',  # Ajusta el ancho y centra el contenido
            'id': 'prefijo',
            'placeholder': '34',  # Placeholder para prefijo
        })
    )


    phone = forms.CharField(
        label="Teléfono",
        max_length=15,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'telefono',
            'placeholder': 'Teléfono',
        })
    )

    message = forms.CharField(
        label="¿En qué te podemos ayudar?",
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'id': 'mensaje',
            'rows': 4,
            'placeholder': '¿En qué te podemos ayudar?',
        })
    )
    privacy_policy = forms.BooleanField(
        label="He leído y acepto la política de privacidad y el aviso legal",
        required=True,
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input',
            'id': 'politicaPrivacidad',
        })
    )
