from django.shortcuts import render
from .models import Blog,Material,Duet
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