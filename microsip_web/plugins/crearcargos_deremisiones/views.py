#encoding:utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from datetime import timedelta
from django.db import connections
from datetime import datetime

#Paginacion
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# user autentication
from .models import *
from .forms import *
from microsip_api.comun.sic_db import get_conecctionname
from django.views.generic.list import ListView

import django_filters

class VentasDocumentoRemisionesListView(ListView):
    context_object_name = "documentos"
    model = VentasDocumento
    template_name = 'ventas/documentos/remisiones_crear_cargos/remisiones.html'
    paginate_by = 20

    def get_queryset(self):
        get_dict = self.request.GET
        form =  SearchForm(self.request.GET)
        documentos = VentasDocumento.objects.filter(tipo='R', estado='P').order_by('-id')
        
        if form.is_valid():
            if 'inicio' in get_dict:
                if get_dict['inicio']:
                    inicio = datetime.strptime(get_dict['inicio'], '%d/%m/%Y')
                    documentos = documentos.filter(fecha__gte=inicio)
            if 'fin' in get_dict:
                if get_dict['fin']:
                    fin = datetime.strptime(get_dict['fin'], '%d/%m/%Y')
                    documentos = documentos.filter(fecha__lte=fin)
            if 'cliente' in get_dict:
                documentos = documentos.filter(cliente__id=get_dict['cliente'])

        return documentos

    def get_context_data(self, **kwargs):
        context = super(VentasDocumentoRemisionesListView, self).get_context_data(**kwargs)
        context['search_form'] = SearchForm(self.request.GET or None)
        return context
    
from django.core import serializers
import json

class generar_cargosbyremisionesview(TemplateView):
    ''' Genera un cargo en cuentas por pagar de las remisiones dadas.'''

    def get(self, request, *args, **kwargs):
        connection_name = get_conecctionname(request.session)
        errors, remisiones_cargadas = [], []

        ids = request.GET['ids']
        ids = map(int, ids[:len(ids)-1].split(','))
        documentos = VentasDocumento.objects.filter(pk__in=ids, cargo_generado=None)
        try:
            concepto = CuentasXCobrarConcepto.objects.get(tipo='V', nombre='Remision')
        except:
            errors.append('Por favor genera un concepto con nombre "Remision" de tipo "Ventas", en microsip - cuentas por cobrar ') 
        else:
            for documento in documentos:
                cxc_documento = CuentasXCobrarDocumento.objects.create(
                    concepto = concepto,
                    fecha =  documento.fecha,
                    cliente = documento.cliente,
                    descripcion = documento.descripcion,
                    cliente_clave = documento.cliente_clave,
                    cobro_importe = 0,
                    tipo_cambio = documento.tipo_cambio,
                    condicion_pago = documento.condicion_pago,
                    descuentoxprontopago_fecha = documento.descuentoxprontopago_fecha,
                    descuentoxprontopago_porcentaje = documento.descuentoxprontopago_porcentaje,
                    creacion_usuario = request.user.username,
                    modificacion_usuario = request.user.username,
                )
                
                impuestos_importes = VentasDocumentoImpuesto.objects.filter(documento= documento).values_list('venta_neta','impuesto','importe','porcentaje','otros')
                iva_retenido, isr_retenido = 0, 0
                importe = 0
                for impuesto_importes in impuestos_importes:
                    
                    impuesto = Impuesto.objects.get(pk=impuesto_importes[1])
                    tipo_impuesto = impuesto.tipoImpuesto
                    if tipo_impuesto.tipo == 'I' and tipo_impuesto.id_interno =='V':
                        importe += impuesto_importes[0]+impuesto_importes[4]
                        
                    if tipo_impuesto.tipo == 'R':
                        if tipo_impuesto.id_interno =='I':
                            iva_retenido += impuesto_importes[2]
                        elif tipo_impuesto.id_interno =='S':
                            isr_retenido += impuesto_importes[2]

                importe_cxc = CuentasXCobrarDocumentoImportes.objects.create(
                    docto_cc = cxc_documento,
                    fecha = documento.fecha,
                    doocumento_acr = cxc_documento,
                    importe = importe,
                    total_impuestos = documento.impuestos_total,
                    iva_retenido =iva_retenido,
                    isr_retenido =isr_retenido,
                )
                
                for impuesto_importes in impuestos_importes:
                    impuesto = Impuesto.objects.get(pk=impuesto_importes[1])
                    tipo_impuesto = impuesto.tipoImpuesto
                    #solo si es tipo IVA
                    if tipo_impuesto.tipo == 'I' and tipo_impuesto.id_interno =='V':
                        CuentasXCobrarDocumentoImportesImpuesto.objects.create(
                            id= -1,
                            importe = importe_cxc,
                            importe_venta_neta = impuesto_importes[0]+impuesto_importes[4],
                            impuesto = impuesto,
                            impuesto_importe = impuesto_importes[2],
                            impuesto_porcentaje = impuesto_importes[3],
                        )
                
                plazos = CondicionPagoPlazo.objects.filter(condicion_de_pago=documento.condicion_pago)
                c = connections[connection_name].cursor()
                for plazo in plazos:
                    plazo_fecha = cxc_documento.fecha + timedelta(days=plazo.dias)    
                    query =  '''INSERT INTO "VENCIMIENTOS_CARGOS_CC" ("DOCTO_CC_ID", "FECHA_VENCIMIENTO", "PCTJE_VEN") VALUES (%s, %s, %s)'''
                    c.execute(query, [cxc_documento.id,  plazo_fecha, plazo.porcentaje_de_venta])
                c.close()

                cxc_documento.aplicado = 'S'
                cxc_documento.save(update_fields=('aplicado',))
                remisiones_cargadas.append(documento.id)
                documento.cargo_generado = True
                documento.save(update_fields=('cargo_generado',))
            
        data = {
            'remisiones_cargadas': remisiones_cargadas,
            'errors': errors,
        }
        data = json.dumps(data)
        return HttpResponse(data, mimetype='application/json')
# Create your views here.
