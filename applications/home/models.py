from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):
    """Modelo para entradas de blog."""

    date_time = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    title = models.CharField(max_length=255,blank=True,null=True)
    category = models.CharField(max_length=255,blank=True,null=True)
    image = models.ImageField(upload_to='images/blog', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField( null=True, blank=True)
    summary = models.TextField( blank=True,null=True)
    avatar = models.ImageField(upload_to='images/avatar', null=True, blank=True)


    def __str__(self):
        """Devuelve el título del post como representación en cadena."""
        return self.title

    def get_summary(self):
        """Devuelve un resumen del cuerpo del post (primeras 200 palabras)."""
        return self.cuerpo[:200]


class Material(models.Model):
    TIPO_CHOICES = [
        ('PELLET','PELLET'),
        ('FILAMENTO','FILAMENTO'),
    ]
    """Modelo para entradas de blog."""
    name = models.CharField(max_length=255,blank=True,null=True)
    image = models.ImageField(upload_to='images/material', null=True, blank=True)
    tipo = models.CharField(
        choices=TIPO_CHOICES,max_length=15
    )
    summary = models.TextField( blank=True,null=True)
    description = models.TextField(max_length=255,blank=True,null=True)

    def __str__(self):
        """Devuelve el título del post como representación en cadena."""
        return self.name

    def get_summary(self):
        """Devuelve un resumen del cuerpo del post (primeras 200 palabras)."""
        return self.description[:200]



class Duet(models.Model):
    TIPO_CHOICES = [
        ('DUET_3DS','DUET_3DS'),
        ('OTRO','OTRO'),
    ]
    """Modelo para entradas de blog."""

    name = models.CharField(max_length=255,blank=True,null=True)
    image1 = models.ImageField(upload_to='images/Duet', null=True, blank=True)
    image2 = models.ImageField(upload_to='images/Duet', null=True, blank=True)
    image3 = models.ImageField(upload_to='images/Duet', null=True, blank=True)
    image4 = models.ImageField(upload_to='images/Duet', null=True, blank=True)
    image5 = models.ImageField(upload_to='images/Duet', null=True, blank=True)
    image6 = models.ImageField(upload_to='images/Duet', null=True, blank=True)
    summary = models.TextField( blank=True,null=True)
    content = models.TextField( null=True, blank=True)


    def __str__(self):
        """Devuelve el título del post como representación en cadena."""
        return self.name

    def get_summary(self):
        """Devuelve un resumen del cuerpo del post (primeras 200 palabras)."""
        return self.content[:200]




class Soporte(models.Model):
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

    name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Nombre")
    number = models.CharField(max_length=255, blank=True, null=True, verbose_name="elija un número")
    image = models.ImageField(upload_to='images/soporte', null=True, blank=True, verbose_name="Imagen")
    video_file = models.FileField(upload_to='media/soporte/videos/', null=True, blank=True, verbose_name="Video")  # Carpeta 'videos/' en MEDIA_ROOT
    tipo_soporte = models.CharField(choices=TIPO_CHOICES, max_length=30, verbose_name="Tipo")
    description = models.TextField(max_length=255, blank=True, null=True, verbose_name="Descripción")

    def __str__(self):
        """Devuelve el nombre como representación en cadena."""
        return self.name or "Sin Nombre"
