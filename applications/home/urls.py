from os import name
from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'home_app'

urlpatterns = [
    path('',
        views.HomePageView.as_view(),
        name='home',
    ),

    path('nx_modular',
        views.NxmodularView.as_view(),
        name='nx_modular',
    ),

    path('bf_modular',
        views.BfmodularView.as_view(),
        name='bf_modular',
    ),

    path('mini_pro',
        views.Mini_proView.as_view(),
        name='mini_pro',
    ),

    path('autoscan-k-3d',
        views.AutoscanView.as_view(),
        name='autoscan-k-3d',
    ),

    path('autoscan-t42',
        views.Autoscant42View.as_view(),
        name='autoscan-t42',
    ),

    path('materiales',
        views.MaterialesView.as_view(),
        name='materiales',
    ),

    path('servicios',
        views.ServiciosView.as_view(),
        name='servicios',
    ),

    path('duet3D',
        views.Duet3DView.as_view(),
        name='duet3D',
    ),

    path('pellet',
        views.PelletView.as_view(),
        name='pellet',
    ),

    path('filamento',
        views.FilamentoView.as_view(),
        name='filamento',
    ),

    path('scantech_ireal_m3',
        views.Irealm3View.as_view(),
        name='scantech_ireal_m3',
    ),

    path('Ireal_it3d',
        views.Irealit3dView.as_view(),
        name='Ireal_it3d',
    ),

    path('Ireal_ze',
        views.IrealzeView.as_view(),
        name='Ireal_ze',
    ),

    path('contacto',
        views.ContactFormView.as_view(),
        name='contacto',
    ),

    path('sobre_nosotros',
        views.NosotrosView.as_view(),
        name='sobre_nosotros',
    ),

    path('informacion',
        views.InformacionView.as_view(),
        name='informacion',
    ),
#apartado de urls para el blog y las publicasiones

    path('blog/',
        views.BlogView.as_view(),
        name='blog_list',
    ),

    path('blog/articulo/<int:pk>/',
        views.BlogDetailView.as_view(),
        name='blog_detail',
    ),

#apartado de las urls para HAZITEk
    path('hazitek_2021',
        views.Hazitek2021View.as_view(),
        name='hazitek_2021',
    ),

    path('hazitek_2022',
        views.Hazitek2022View.as_view(),
        name='hazitek_2022',
    ),

    path('hazitek_2023',
        views.Hazitek2023View.as_view(),
        name='hazitek_2023',
    ),

    path('hazitek_2024',
        views.Hazitek2024View.as_view(),
        name='hazitek_2024',
    ),
#apartado para las urls de los materiales

    path('pellet/detalle/<int:pk>/',
        views.PelletDetailView.as_view(),
        name='pellet_detail',
    ),

    path('filamento/detalle/<int:pk>/',
        views.FilamentoDetailView.as_view(),
        name='filamento_detail',
    ),

    path('formulario_pedidos',
        views.formulariopedidosTemplateView.as_view(),
        name='formulario_pedidos',
    ),
#politicas y consentimientos 

    path('cookies',
        views.CookiesView.as_view(),
        name='cookies',
    ),

    path('politica_de_privacidad',
        views.Politica_de_privacidadView.as_view(),
        name='politica_de_privacidad',
    ),

    path('aviso_legal',
        views.Aviso_legalView.as_view(),
        name='aviso_legal',
    ),

#url para el apartado de scaners 3D

    path('mscan_l15',
        views.Mscan_l15View.as_view(),
        name='mscan_l15',
    ),

    path('trackscanp42',
        views.Trackscanp42View.as_view(),
        name='trackscanp42',
    ),

    path('aviso_legal',
        views.Aviso_legalView.as_view(),
        name='aviso_legal',
    ),

    path('aviso_legal',
        views.Aviso_legalView.as_view(),
        name='aviso_legal',
    ),

    path('aviso_legal',
        views.Aviso_legalView.as_view(),
        name='aviso_legal',
    ),

#apartado de urls para la seccino de DUET

    path('duet/articulo/<int:pk>/',
         views.DuetDetailView.as_view(),
         name='duet_articulo'),

    path('materiales_validados',
        views.Materiales_validadosView.as_view(),
        name='materiales_validados',
    ),

    path('servicio_validacion',
        views.Servicio_validadacionView.as_view(),
        name='servicio_validacion',
    ),

    path('alimentador_pellet',
        views.Alimetador_pelletView.as_view(),
        name='alimentador_pellet',
    ),

    path('soporte_tecnico',
        views.Soporte_tecnicoView.as_view(),
        name='soporte_tecnico',
    ),


    path('soporte_detail/<int:pk>/',
        views.SoporteDetailView.as_view(),
        name='soporte_detail',
    ),


    path('soporte_manual',
        views.Soporte_manualView.as_view(),
        name='soporte_manual',
    ),

]