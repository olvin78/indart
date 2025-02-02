from django.shortcuts import render
from django.core.mail import send_mail
from django.urls import reverse_lazy
from .forms import ContactForm,Solicitud_impresionForm
from django.db.models import Q

from .models import Blog,Material,Duet,Soporte
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    FormView
)




class HomePageView(ListView):
    template_name="home/index.html"
    model = Blog
    context_object_name = 'datos'
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('-date_time')[:3]

class NxmodularView(TemplateView):
    template_name="home/nx_modular.html"

class BfmodularView(TemplateView):
    template_name="home/bf_modular.html"

class AutoscanView(TemplateView):
    template_name="home/autoScan-k-3D.html"

class Autoscant42View(TemplateView):
    template_name="home/autoScan-t42.html"

class MaterialesView(TemplateView):
    template_name="home/materiales.html"

class ServiciosView(TemplateView):
    template_name="home/servicios.html"

class Irealm3View(TemplateView):
    template_name="home/acanerAcolo-ireal_m3.html"

class Irealit3dView(TemplateView):
    template_name="home/scanerAcolor_it3d.html"

class IrealzeView(TemplateView):
    template_name="home/irealze.html"

class ContactoView(TemplateView):
    template_name="home/contacto.html"

class NosotrosView(TemplateView):
    template_name="home/sobre_nosotros.html"

class InformacionView(TemplateView):
    template_name="home/informacion.html"

class Mini_proView(TemplateView):
    template_name="home/mini_pro.html"

class Hazitek2021View(TemplateView):
    template_name="home/hazitek_2021.html"

class Hazitek2022View(TemplateView):
    template_name="home/hazitek_2022.html"

class Hazitek2023View(TemplateView):
    template_name="home/hazitek_2023.html"

class Hazitek2024View(TemplateView):
    template_name="home/hazitek_2024.html"


class formulariopedidosTemplateView(TemplateView):
    template_name="home/form_pedidos.html"



class Duet3DView(ListView):
    template_name="home/duet3d.html"
    model = Duet
    context_object_name = 'datos'

    def get_queryset(self):
        """Filtra los datos si hay una búsqueda"""
        queryset = Duet.objects.all()
        search_query = self.request.GET.get('q')  # Obtener el parámetro de búsqueda

        if search_query:
            queryset = queryset.filter(Q(name__icontains=search_query) | Q(summary__icontains=search_query))

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_query = self.request.GET.get('q', '')

        context["search_query"] = search_query  # Mantener el valor de búsqueda en el input
        
        # Si no hay resultados en la búsqueda, mostrar un mensaje
        if search_query and not context["datos"]:  
            context["no_results_message"] = f"Oops! No se encontraron resultados para '{search_query}'."

        return context



class PelletView(ListView):
    template_name="home/pellet.html"
    model = Material
    context_object_name = 'datos'
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(tipo='PELLET').order_by('id')

class FilamentoView(ListView):
    template_name="home/filamento.html"
    model = Material
    context_object_name = 'datos'
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(tipo='FILAMENTO').order_by('id')



#este es el template para el blog
class BlogView(ListView):
    template_name="home/blog.html"
    model = Blog
    context_object_name = 'datos'
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('-date_time')


class BlogDetailView(DetailView):
    model = Blog # Especifica el modelo Blog
    template_name = 'home/articulo_completo.html' # Define el template "articulo_completo.html"
    context_object_name = 'datos'

class PelletDetailView(DetailView):
    model = Material # Especifica el modelo Blog
    template_name = 'home/pellet_detalle.html' # Define el template "articulo_completo.html"
    context_object_name = 'datos'

class FilamentoDetailView(DetailView):
    model = Material # Especifica el modelo Blog
    template_name = 'home/filamento_detalle.html' # Define el template "articulo_completo.html"
    context_object_name = 'datos'

class CookiesView(TemplateView):
    template_name="home/cookies.html"

class Politica_de_privacidadView(TemplateView):
    template_name="home/politica_de_privacidad.html"

class Aviso_legalView(TemplateView):
    template_name="home/aviso_legal.html"

class Mscan_l15View(TemplateView):
    template_name="home/portatil_mscan_l15.html"

class Trackscanp42View(TemplateView):
    template_name="home/portatil_trackScan_p42.html"


class DuetDetailView(DetailView):
    model = Duet # Especifica el modelo Duet
    template_name = 'home/duet_detalle.html' # Define el template "articulo_completo.html"
    context_object_name = 'datos'


class Materiales_validadosView(TemplateView):
    template_name="home/materiales_validados.html"

class Servicio_validadacionView(TemplateView):
    template_name="home/servicio_validacion.html"

class Alimetador_pelletView(TemplateView):
    template_name="home/alimetador_de_pellet.html"



class Soporte_tecnicoView(ListView):
    model = Soporte  # Especifica el modelo correcto
    template_name = "home/soporte_tecnico.html"  # Especifica la plantilla
    context_object_name = 'datos'  # Nombre del contexto para la plantilla
    def get_context_data(self, **kwargs):
        # Llama al método original para obtener el contexto base
        context = super().get_context_data(**kwargs)
        
        # Agrega los datos de otros modelos al contexto paa ver el mapa en el index
        context['Interfaz_Web'] = Soporte.objects.filter(tipo_soporte='Interfaz_Web')
        context['Simpify'] = Soporte.objects.filter(tipo_soporte='Simpify')
        context['Cabezal_DART'] = Soporte.objects.filter(tipo_soporte='Cabezal_DART')
        context['Cabezal_DD_HR'] = Soporte.objects.filter(tipo_soporte='Cabezal_DD_HR')
        context['Cabezal_Pellet'] = Soporte.objects.filter(tipo_soporte='Cabezal_Pellet')
        context['Mantenimiento'] = Soporte.objects.filter(tipo_soporte='Mantenimiento')
        context['Firmware'] = Soporte.objects.filter(tipo_soporte='Firmware')
        context['Manejo_de_impresoras'] = Soporte.objects.filter(tipo_soporte='Manejo_de_impresoras')
        context['Super_slicer'] = Soporte.objects.filter(tipo_soporte='Super_slicer')

        return context


class SoporteDetailView(DetailView):
    model = Soporte
    template_name = 'home/soporte_tecnico_detail.html'
    context_object_name = 'datos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Convertir a entero para evitar errores
        try:
            numactual = int(self.object.number)
            tipoactual = self.object.tipo_soporte
            context['numero_siguiente'] = Soporte.objects.filter(tipo_soporte=tipoactual,number=str(numactual + 1)).first()
        except ValueError:
            context['numero_siguiente'] = None  # Si el campo no es un número, evitar errores
        
        try:
            tipoactual = self.object.tipo_soporte
            context['numero_primero'] = Soporte.objects.filter(tipo_soporte=tipoactual).first()
        except ValueError:
            context['numero_primero'] = None 
        return context




#esta es la vista para el formulario de conttacto
class ContactFormView(FormView):
    template_name = 'home/contacto.html'  # El template donde se renderiza el formulario
    form_class = ContactForm  # El formulario que definiste
    success_url = reverse_lazy('home_app:contacto')  # Redirección tras el envío exitoso

    def form_valid(self, form):
        # Extrae los datos del formulario
        name = form.cleaned_data['name']
        company = form.cleaned_data['company']
        email = form.cleaned_data['email']
        country = form.cleaned_data['country']
        prefix = form.cleaned_data['prefix']
        phone = form.cleaned_data['phone']
        message = form.cleaned_data['message']
        privacy_policy = form.cleaned_data['privacy_policy']

        # Construye el mensaje
        subject = f"Nuevo mensaje de contacto de {name}"
        message_body = f"Nombre: {name}\nCorreo: {email}\n\nMensaje:\n{message}"

        # Envía el correo
        send_mail(
            subject,
            message_body,
            'euskodev@gmail.com',  # Remitente (cambia esto por un correo válido)
            ['euskodev@gmail.com'],  # Destinatarios
        )

        return super().form_valid(form)


class Soporte_manualView(TemplateView):
    template_name="home/soporte_manual_configuracion.html"


#esta es la vista para el formulario para hacer un pedido de impresion
class Solicitud_impresionFormView(FormView):
    template_name = 'home/form_impresion.html'  # El template donde se renderiza el formulario
    form_class = Solicitud_impresionForm  # El formulario que definiste
    success_url = reverse_lazy('home_app:contacto')  # Redirección tras el envío exitoso

    def form_valid(self, form):
        # Extrae los datos del formulario
        name = models.CharField("Nombre", max_length=255)
        apellido = models.CharField("Apellido", max_length=255)
        company = models.CharField("Empresa", max_length=255, blank=True, null=True)
        email = models.EmailField("Email")
        country = models.CharField("País", max_length=255)
        prefix = models.CharField("Prefijo", max_length=5)
        phone = models.CharField("Teléfono", max_length=15)
        image = models.ImageField("Imagen", upload_to="impresiones/")
        message = models.TextField("¿En qué te podemos ayudar?")
        cantidad = models.CharField("Cantidad", max_length=15)
        description = models.TextField("Descripción", max_length=1000)
        privacy_policy = models.BooleanField("He leído y acepto la política de privacidad y el aviso legal")


        # Construye el mensaje
        subject = f"Nuevo mensaje de contacto de {name}"
        message_body = f"Nombre: {name}\nCorreo: {email}\n\nMensaje:\n{message}"

        # Envía el correo
        send_mail(
            subject,
            message_body,
            'euskodev@gmail.com',  # Remitente (cambia esto por un correo válido)
            ['euskodev@gmail.com'],  # Destinatarios
        )

        return super().form_valid(form)
