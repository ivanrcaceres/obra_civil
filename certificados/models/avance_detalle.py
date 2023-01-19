# -*- coding: utf-8 -*-

from odoo import models, fields, api


class avance_detalle(models.Model):
    _name = "certificados.avance_detalle"

    product_id = fields.Many2one('product.template')
    # unidad_de_medida = fields.Many2one('product.uom')
    # price_unit = fields.Float('Precio Unitario')
    quantity = fields.Float('Cantidad Hechas')
    project_id = fields.Many2one('project.project')

    avance_id = fields.Many2one('certificados.avance')


    @api.onchange('project_id','product_id')
    def definir_dominio(self):

        if self.project_id:
            servi = self.env['certificados.proyecto_detalle_servicio'].search([('project_id','=',self.project_id.id)])
            product = servi.mapped('product_id').mapped('id')
            return {'domain': {'product_id': [('id', 'in', product)]}}