# -*- coding: utf-8 -*-
import io

from odoo.http import request
from odoo import fields, models, exceptions, api
from datetime import datetime, timedelta, time, date
# -*- coding: utf-8 -*-
from odoo import http
# from django.http.response import JsonResponse, HttpResponse
from string import ascii_uppercase

from openpyxl import Workbook
from openpyxl.styles import Font, Border, Alignment, Side, PatternFill
from openpyxl import Workbook

import xlwt
import base64
import xlsxwriter
from io import StringIO



from odoo.addons.web.controllers.main import serialize_exception,content_disposition

# -*- coding: utf-8 -*-
import io

from odoo.addons.web.controllers.main import serialize_exception,content_disposition

from odoo.http import request
from odoo import fields, models, exceptions, api
from datetime import datetime, timedelta, time, date
# -*- coding: utf-8 -*-
from odoo import http
# from django.http.response import JsonResponse, HttpResponse
from string import ascii_uppercase

from openpyxl import Workbook
from openpyxl.styles import Font, Border, Alignment, Side, PatternFill
from openpyxl import Workbook

import xlwt
import base64
import xlsxwriter


# -*- coding: utf-8 -*-
from odoo import fields, models, exceptions, api
from datetime import datetime, timedelta,time


class WizardReporteCertificadoProyecto(models.TransientModel):

    _name = 'certificados.wizard_reporte_certificado_proyecto'

    # desde = fields.Date(string="Fecha desde")
    # hasta = fields.Date(string="Fecha hasta")


    # journal_ids = fields.Many2many('certificados.avances', string="Diarios",
    #                                default=lambda self: self._get_default_avances())
    # avance_ids = fields.One2many('certificados.avance', string='Avance')
    # cliente_id = fields.Many2one('res.partner')
    proyecto_id = fields.Many2one('project.project', default=lambda self: self._get_default_proyecto())
    avance_ids = fields.Many2many('certificados.avance', 'wizard_reporte_certificado_proyecto_ids', string='Avances Finales')

    # cajas_ids=fields.Many2many('ruc.cajas',domain=[('state', '=', 'cerrado')])
    # cantidad_cajas=fields.Integer()

    @api.model
    def _get_default_proyecto(self):
        proyecto = self.env['project.project'].browse(self._context.get('active_id'))
        return proyecto


    @api.multi
    def check_report(self):
        data = {}
        data['form'] = self.read(['desde', 'hasta'])[0]
        return self._print_report(data)

    def _print_report(self, data):
        data['form'].update(self.read(['desde', 'hasta'])[0])
        # return self.env.ref('certificados.action_reporte_certificados_wizard').report_action(self, data)
        return self.env.ref('certificados.report_certificado01_action').report_action(self, data)

    def excel(self):
        print (self._context.get('active_id'))
        data = {}
        data['form'] = self.read(['desde', 'hasta', 'avance_ids'])[0]
        print (data)
        print (data['form']['avance_ids'][0])

        palabra = str(self._context.get('active_id'))
        for a in data['form']['avance_ids']:
            print (a)
            palabra = palabra + '-' + str(a)


        print (palabra)

        x = palabra.split('-')
        x[0] = str(self._context.get('active_id'))
        print (x)
        for aux in x:
            if aux != '':
                print (aux)

        return {
                'type': 'ir.actions.act_url',
                'url': '/certificados/certificados/'+str(palabra),
                'target': 'self'
                }


class ReporteCobranzas(models.AbstractModel):
    _name = 'report.certificados.report_certificado01'

    @api.model
    def get_report_values(self, docids, data=None):
        self.model = self.env.context.get('active_model')
        docs = self.env[self.model].browse(self.env.context.get('active_id'))

        print (data)

        docargs = {
            'doc_ids': self.ids,
            'doc_model': self.model,
            'docs': docs,
            # 'time': time,
            # 'cobros': list_cobros_general

        }
        return docargs



