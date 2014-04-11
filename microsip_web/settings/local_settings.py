MICROSIP_MODULES = (
    'microsip_api.apps.config',
    'microsip_web.libs.api',
    'microsip_web.apps.main',
    # 'microsip_web.apps.main.filtros',
    # 'microsip_web.apps.main.comun.articulos',
    # # 'microsip_web.apps.main.comun.articulos.articulos.alertas',
    # 'microsip_web.apps.main.comun.listas',
    # 'microsip_web.apps.main.comun.otros',
    # 'microsip_web.apps.main.comun.clientes',
    # 'microsip_web.apps.main.comun.clientes.clientes.cliente_articulos',
    'microsip_web.apps.ventas',
    # 'microsip_web.apps.ventas.documentos',
    # 'microsip_web.apps.ventas.herramientas.generar_polizas',
    
    # 'microsip_web.apps.inventarios',
    # 'microsip_web.apps.compras',
    # 'microsip_web.apps.cuentas_por_pagar',
    # 'microsip_web.apps.cuentas_por_pagar.herramientas.generar_polizas',
    # 'microsip_web.apps.cuentas_por_cobrar',
    # 'microsip_web.apps.cuentas_por_cobrar.herramientas.generar_polizas',
    # 'microsip_web.apps.punto_de_venta',    
    # 'microsip_web.apps.punto_de_venta.puntos',
)

# microsip_modules_dic={
#     'apps':[
#         {'main':[ {'comun':['articulos','listas','otros','clientes']}, ], },
#         {'ventas':[
#             {'documentos':['remisiones','facturas']},
#             {'herramientas':['generar_polizas','preferencias']},
#         ]},
#     ]
#     'plugins':[
#         {'crearcargos_deremisiones':{'url':r'ventas/remisiones_cxc/',}, },
#     ]
# }

MICROSIP_PLUGINS = (
    {
        'app': 'microsip_web.plugins.crearcargos_deremisiones',
        'url_main_path':r'ventas/remisiones_cxc/',
    },
)