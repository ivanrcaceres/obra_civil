# -*- coding: utf-8 -*-

from odoo import models, fields, api

class contrato_contratista_detalle(models.Model):
    _name = "certificados.contrato_contratista_detalle"

    product_id = fields.Many2one('product.template')
    unidad_de_medida = fields.Many2one('product.uom')
    price_unit = fields.Float('Precio Unitario')
    quantity = fields.Float('Cantidad')

    contrato_contratista_id = fields.Many2one('certificados.contrato_contratista')