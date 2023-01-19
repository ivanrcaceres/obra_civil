# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Contrato_cliente(models.Model):
    _name = "certificados.contrato_cliente"

    name = fields.Char(string='Nombre o Titulo')
    fecha_fin = fields.Date(string='Fecha de finalizacion de la obra')
    cliente_id = fields.Many2one('res.partner', string='Cliente')
    descripcion = fields.Text('Descripcion de la obra')
    state = fields.Selection([('borrador', 'Borrador'), ('iniciado', 'Iniciado'), ('finalizado', 'Finalizado'), ('rescision', 'Rescision')], 'Estado', default='borrador')
    contrato_cliente_detalle_ids = fields.One2many('certificados.contrato_cliente_detalle','contrato_cliente_id', string='Detalle de los servicios')
    project_ids = fields.One2many('project.project', 'contrato_cliente_id', string='Proyectos',store=True)
    project2_ids = fields.One2many('certificados.detalle_proyectos', 'contrato_cliente_id', string='Proyectos')

    @api.multi
    def borrador(self):
        self.state = 'borrador'

    @api.multi
    def iniciado(self):
        self.state = 'iniciado'

    @api.multi
    def finalizado(self):
        self.state = 'finalizado'

    @api.multi
    def rescision(self):
        self.state = 'rescision'

