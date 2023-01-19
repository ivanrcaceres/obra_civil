# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Contrato_cliente(models.Model):
    _name = "certificados.quincena"

    name = fields.Char(string='Nombre')
    fecha = fields.Date(string='Fecha de la quincena')
    observacion = fields.Text(string = 'Observacion')

    project_id = fields.Many2one('project.project')