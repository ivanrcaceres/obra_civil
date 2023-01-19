# -*- coding: utf-8 -*-

from odoo import models, fields, api

class contrato_contratista(models.Model):
    _name = "certificados.contrato_contratista"

    name = fields.Char(string='Nombre o Titulo')
    fecha = fields.Date()
    contratista_id = fields.Many2one('res.partner', string='Contratista')

    contrato_contratista_detalle_ids = fields.One2many('certificados.contrato_contratista_detalle', 'contrato_contratista_id', string='Detalle')
    # lugar_ids = fields.One2many('obra_civil_3.lugar', 'contrato_id', string='Detalle')
    # quincena_ids = fields.One2many('obra_civil_3.quincena', 'contrato_id', string='Detalle')
    # avance_ids = fields.One2many('obra_civil_3.avance', 'contrato_id', string='Avance')