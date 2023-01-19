# -*- coding: utf-8 -*-

from odoo import models, fields, api

class detalle_proyectos(models.Model):
    _name = "certificados.detalle_proyectos"

    proyecto_id = fields.Many2one('project.project')
    contrato_cliente_id = fields.Many2one('certificados.contrato_cliente')