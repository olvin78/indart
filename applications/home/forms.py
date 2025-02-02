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

"""este es le formulario para  el formualario dwesolicitar impresion"""

class Solicitud_impresionForm(forms.Form):
    name = forms.CharField(
        label="Nombre",
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control rounded-pill',  # Borde redondeado
            'id': 'nombre',
            'placeholder': 'Escriba su Nombre',
            'style': 'font-size: 18px; height: 50px; border: 2px solid #1e7f86; padding-left: 20px;'
        })
    )

    apellido = forms.CharField(
        label="Apellido",
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control rounded-pill',  # Bordes redondeados
            'id': 'apellido',  # ✅ ID corregido (antes era "nombre")
            'placeholder': 'Escriba su Apellido',
            'style': 'font-size: 18px; height: 50px; border: 2px solid #1e7f86; padding-left: 20px;'
        })
    )

    company = forms.CharField(
        label="Empresa",
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control rounded-pill',  # Bordes redondeados
            'id': 'empresa',
            'placeholder': 'Empresa',
            'style': 'font-size: 18px; height: 50px; border: 2px solid #1e7f86; padding-left: 20px;'
        })
    )

    email = forms.EmailField(
        label="Email",
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control rounded-pill',
            'id': 'email',
            'placeholder': 'Email',
            'style': 'font-size: 18px; height: 50px; border: 2px solid #1e7f86; padding-left: 20px;'
        })
    )

    country = forms.CharField(
        label="País",
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control rounded-pill',
            'id': 'pais',
            'placeholder': 'Escribe tu país',
            'style': 'font-size: 18px; height: 50px; border: 2px solid #1e7f86; padding-left: 20px;'
        })
    )

    prefix = forms.CharField(
        label="Prefijo",
        max_length=5,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control text-center rounded-pill',
            'id': 'prefijo',
            'placeholder': '+34',
            'style': 'font-size: 18px; height: 50px; border: 2px solid #1e7f86; max-width: 90px; text-align: center;'
        })
    )

    phone = forms.CharField(
        label="Teléfono",
        max_length=15,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control rounded-pill',
            'id': 'telefono',
            'placeholder': 'Teléfono',
            'style': 'font-size: 18px; height: 50px; border: 2px solid #1e7f86; padding-left: 15px;'
        })
    )

    image = forms.ImageField(
    label="Imagen",
    required=True,  
    widget=forms.ClearableFileInput(attrs={
        'class': 'form-control rounded-pill',
        'id': 'imagen',
        'accept': 'image/*',  
        'style': 'font-size: 16px; height: 50px; border: 2px solid #1e7f86; padding: 10px; background-color: #f1f1f1;'
    })
    )

    message = forms.CharField(
        label="¿En qué te podemos ayudar?",
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'form-control rounded',
            'id': 'mensaje',
            'rows': 4,
            'placeholder': '¿En qué te podemos ayudar?',
            'style': 'font-size: 18px; height: 120px; border: 2px solid #1e7f86; padding: 10px; background-color: #f1f1f1; resize: vertical;'
        })
    )

    cantidad = forms.CharField(
        label="Cantidad",
        max_length=15,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control rounded-pill',
            'id': 'cantidad',
            'placeholder': 'Ingrese la cantidad',
            'style': 'font-size: 18px; height: 50px; border: 2px solid #1e7f86; padding-left: 20px; background-color: #f1f1f1;'
        })
    )

    description = forms.CharField(
        label="Descripción",
        max_length=1000,  
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'form-control rounded',
            'id': 'descripcion',
            'placeholder': 'Escribe aquí...',
            'rows': 5,
            'style': 'font-size: 18px; height: 140px; border: 2px solid #1e7f86; padding: 10px; background-color: #f1f1f1; resize: vertical;'
        })
    )

    privacy_policy = forms.BooleanField(
        label="He leído y acepto la política de privacidad y el aviso legal",
        required=True,
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input',
            'id': 'politicaPrivacidad',
            'style': 'width: 18px; height: 18px; border: 2px solid #1e7f86;'
        })
    )
