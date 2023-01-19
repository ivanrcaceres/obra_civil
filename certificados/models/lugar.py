# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Contrato_cliente(models.Model):
    _name = "certificados.lugar"

    name = fields.Char(string='Nombre')
    descripcion = fields.Text(string='Descripcion')

    project_id = fields.Many2one('project.project')