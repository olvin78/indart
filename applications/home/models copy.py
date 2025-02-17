from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from parler.models import TranslatableModel, TranslatedFields


class Blog(TranslatableModel):  # ✅ Ahora es traducible
    """Modelo para entradas de blog."""

    translations = TranslatedFields(
        title=models.CharField(max_length=255, blank=True, null=True),
        category=models.CharField(max_length=255, blank=True, null=True),
        content=HTMLField(null=True, blank=True),
        summary=HTMLField(blank=True, null=True),
    )

    date_time = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(upload_to='images/blog', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='images/avatar', null=True, blank=True)

    def __str__(self):
        return self.safe_translation_getter('title', any_language=True)


class Material(TranslatableModel):  # ✅ Ahora es traducible
    """Modelo para Materiales."""

    TIPO_CHOICES = [
        ('PELLET', 'PELLET'),
        ('FILAMENTO', 'FILAMENTO'),
    ]

    translations = TranslatedFields(
        name=models.CharField(max_length=255, blank=True, null=True),
        summary=HTMLField(blank=True, null=True),
        description=HTMLField(blank=True, null=True),
    )

    image = models.ImageField(upload_to='images/material', null=True, blank=True)
    tipo = models.CharField(choices=TIPO_CHOICES, max_length=15)

    def __str__(self):
        return self.safe_translation_getter('name', any_language=True)


class Duet(TranslatableModel):  # ✅ Ahora es traducible
    """Modelo para Duet."""

    TIPO_CHOICES = [
        ('DUET_3DS', 'DUET_3DS'),
        ('OTRO', 'OTRO'),
    ]

    translations = TranslatedFields(
        name=models.CharField(max_length=255, blank=True, null=True),
        summary=HTMLField(blank=True, null=True),
        content=HTMLField(blank=True, null=True),
    )

    images = models.JSONField(blank=True, null=True, default=list)
    image1 = models.ImageField(upload_to='images/Duet', null=True, blank=True)
    image2 = models.ImageField(upload_to='images/Duet', null=True, blank=True)
    image3 = models.ImageField(upload_to='images/Duet', null=True, blank=True)
    image4 = models.ImageField(upload_to='images/Duet', null=True, blank=True)
    image5 = models.ImageField(upload_to='images/Duet', null=True, blank=True)
    image6 = models.ImageField(upload_to='images/Duet', null=True, blank=True)

    def __str__(self):
        return self.safe_translation_getter('name', any_language=True)


class Soporte(TranslatableModel):  # ✅ Ahora es traducible
    """Modelo para Soporte."""

    TIPO_CHOICES = [
        ('Interfaz_Web', 'Interfaz_Web'),
        ('Simpify', 'Simpify'),
        ('Cabezal_DART', 'Cabezal_DART'),
        ('Cabezal_DD_HR', 'Cabezal_DD_HR'),
        ('Cabezal_Pellet', 'Cabezal_Pellet'),
        ('Mantenimiento', 'Mantenimiento'),
        ('Firmware', 'Firmware'),
        ('Manejo_de_impresoras', 'Manejo_de_impresoras'),
        ('Super_slicer', 'Super_slicer'),
    ]

    translations = TranslatedFields(
        name=models.CharField(max_length=255, blank=True, null=True, verbose_name="Nombre"),
        description=HTMLField(max_length=255, blank=True, null=True, verbose_name="Descripción"),
    )

    number = models.CharField(max_length=255, blank=True, null=True, verbose_name="Elija un número")
    image = models.ImageField(upload_to='images/soporte', null=True, blank=True, verbose_name="Imagen")
    video_file = models.FileField(upload_to='media/soporte/videos/', null=True, blank=True, verbose_name="Video")
    tipo_soporte = models.CharField(choices=TIPO_CHOICES, max_length=30, verbose_name="Tipo")
    urlyoutube = models.URLField(max_length=255, blank=True, null=True, verbose_name="URL de video de YouTube")

    def __str__(self):
        return self.safe_translation_getter('name', any_language=True)
