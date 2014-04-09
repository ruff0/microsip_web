
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.views import generic
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from  microsip_web.settings.prod import MICROSIP_MODULES, MICROSIP_PLUGINS

dajaxice_autodiscover()
import autocomplete_light
autocomplete_light.autodiscover()

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
    #main
    url(r'', include('microsip_web.apps.main.urls', namespace='main')),
    url(r'autocomplete/', include('autocomplete_light.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #LOGIN
    url(r'^select_db/$','microsip_web.apps.inventarios.views.select_db'),    
    url(r'^login/$','microsip_web.apps.inventarios.views.ingresar'),
    url(r'^logout/$', 'microsip_web.apps.inventarios.views.logoutUser'),
)

if 'microsip_web.apps.inventarios' in MICROSIP_MODULES:
    urlpatterns += url(r'^inventarios/', include('microsip_web.apps.inventarios.urls', namespace='Inventarios')),

urlpatterns += url(r'^ventas/', include('microsip_web.apps.ventas.urls', namespace='ventas')),

if 'microsip_web.apps.punto_de_venta' in MICROSIP_MODULES:
    urlpatterns += url(r'^punto_de_venta/', include('microsip_web.apps.punto_de_venta.urls', namespace='punto_de_venta')),

if 'microsip_web.apps.cuentas_por_cobrar' in MICROSIP_MODULES:
    urlpatterns += url(r'^cuentas_por_cobrar/', include('microsip_web.apps.cuentas_por_cobrar.urls', namespace='cuentas_por_cobrar')),

if 'microsip_web.apps.cuentas_por_pagar' in MICROSIP_MODULES:
    urlpatterns += url(r'^cuentas_por_pagar/', include('microsip_web.apps.cuentas_por_pagar.urls', namespace='cuentas_por_pagar')),

if 'microsip_web.apps.contabilidad' in MICROSIP_MODULES:
    urlpatterns += url(r'^contabilidad/', include('microsip_web.apps.contabilidad.urls', namespace='contabilidad')),

if 'microsip_web.apps.compras' in MICROSIP_MODULES:
    urlpatterns += url(r'^compras/', include('microsip_web.apps.compras.urls', namespace='compras')),
    # urlpatterns += url(r'^compras/', include('microsip_web.apps.compras.documentos.compras.urls', namespace='compras_doc_compras')),
    # urlpatterns += url(r'^compras/', include('microsip_web.apps.compras.documentos.ordenes.urls', namespace='compras_doc_ordenes')),

if 'microsip_web.apps.punto_de_venta.puntos' in MICROSIP_MODULES:
    urlpatterns += url(r'punto_de_venta/', include('microsip_web.apps.punto_de_venta.puntos.urls', namespace='pv_puntos')),

for plugin in MICROSIP_PLUGINS:
        # urlpatterns += url(plugin['url_main_path'], include(plugin['app']+'.urls', namespace='plugins_remisiones_cxc')),
    urlpatterns += url(plugin['url_main_path'], include(plugin['app']+'.urls', namespace='plugins_remisiones_cxc')),

urlpatterns += staticfiles_urlpatterns()