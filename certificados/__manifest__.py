# -*- coding: utf-8 -*-
{
    'name': "certificados",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','product','project'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/contrato_cliente.xml',
        'views/contrato_cliente_detalle.xml',
        'views/product_herencia.xml',
        'views/proyecto_herencia.xml',
        'views/contrato_contratista.xml',
        'views/contrato_contratista_detalle.xml',
        'views/proyecto_detalle_servicio.xml',
        'views/lugar.xml',
        'views/quincena.xml',
        'views/avance.xml',
        'views/avance_detalle.xml',
        'views/detalle_proyectos.xml',

        'reports/certificados_reports.xml',
        'reports/report_certificado01.xml',

        'wizard/wizard_report_certificado_proyecto.xml',
        'wizard/wizard_report_certificado_cliente.xml'



        # 'wizard/wizard_report_certificado_proyecto.xml'

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml'
    ],
}