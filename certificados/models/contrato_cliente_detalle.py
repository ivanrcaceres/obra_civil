# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Contrato_cliente_detalle(models.Model):
    _name = "certificados.contrato_cliente_detalle"

    product_id = fields.Many2one('product.template')
    unidad_de_medida = fields.Many2one('product.uom')
    price_unit = fields.Float('Precio Unitario')
    quantity = fields.Float('Cantidad')
    subtotal = fields.Float('Subtotal')

    cantidades_hechas = fields.Float('Hechas en Unid. Med.')
    subtotales_hechas = fields.Float('Hechas en Dinero')

    # relaciones
    # contrato_id = fields.Many2one('obra_civil_3.contrato')
    contrato_cliente_id = fields.Many2one('certificados.contrato_cliente')





    # @api.onchange('product_id')
    # def _onchange_unidaddemedida(self):
    #     if self.product_id != '':
    #         self.unidad_de_medida = self.product_tmpl_id.uom_id
    #         print ('onchange del producto 1')
    #     else:
    #         self.unidad_de_medida = self.product_tmpl_id.uom_id
    #         print ('onchange del producto 2')



    # @api.onchange('price_unit', 'quantity')
    # def _onchange_priceunit_quantity(self):
    #     # set auto-changing field
    #     self.subtotal = self.price_unit * self.quantity
    #     print ('onchange del precio unitario y cantidad')
    #     print (self.price_unit)
    #     print (self.quantity)