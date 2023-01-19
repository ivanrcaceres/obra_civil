# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _

class Producto(models.Model):
    _inherit = 'product.template'
    serviciodeobra = fields.Boolean(default=True, string='Servicio de Obra')