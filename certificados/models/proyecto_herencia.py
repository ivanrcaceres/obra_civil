# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _

class Proyecto(models.Model):
    _inherit = 'project.project'
    descripcion = fields.Text()
    label_tasks = fields.Char(default='Tarea')
    contrato_cliente_id = fields.Many2one('certificados.contrato_cliente')
    # contrato_contratista_id = fields.Many2one('certificados.contrato_contratista', string='Contrato con el contratista')
    contratista_id = fields.Many2one('res.partner', string='Contratista')
    fecha_de_inicio = fields.Date(string='Fecha de inicio de la obra')
    fecha_de_fin = fields.Date(string='Fecha de finalizacion de la obra')
    monto_no_exceder = fields.Float(string="Monto a no exceder")
    monto_total_hecho = fields.Float(string="Monto hecho", compute='monto_hecho')

    proyecto_detalle_servicio_ids = fields.One2many('certificados.proyecto_detalle_servicio', 'project_id', string='Servicios de la obra')
    lugar_ids = fields.One2many('certificados.lugar', 'project_id', string='Lugar')
    quincena_ids = fields.One2many('certificados.quincena', 'project_id', string='Quincena')
    avance_ids = fields.One2many('certificados.avance', 'project_id', string='Avance')


    @api.one
    def monto_hecho(self):
        self.quantity_hechas = 1 * 10 * 2
        # self.quantity_hechas = 1*10
        a = self.env['certificados.proyecto_detalle_servicio'].search([('project_id', '=', self.id)])
        suma = 0
        for b in a:
            suma = suma + b.montohechos
        self.monto_total_hecho = suma