# -*- coding: utf-8 -*-

from odoo import models, fields, api


class contratodetalle(models.Model):
    _name = "obra_civil_2.contratodetalle"

    product_id = fields.Many2one('product.product', 'Servicio')
    unidad_de_medida = fields.Char()
    precio = fields.Float()
    quantity = fields.Float('Cantidad')
    subtotal = fields.Float('Subtotal')
    contrato_id = fields.Many2one('obra_civil_2.contrato')

    @api.model
    def create(self, vals):
        producto = super(contratodetalle, self).create(vals)
        self.env['obra_civil_2.resumendetalle'].create({
            'product_id': vals['product_id'],
            'quantity': vals['quantity'],
            'contrato_id': vals['contrato_id'],
        })
        # print('pppppp')
        # print(self.id)
        # print(self.contrato_id)
        # print(vals)
        return producto


    @api.onchange('product_id')
    def _onchange_producto_id(self):
        self.unidad_de_medida = self.product_id.uom_id.name

    @api.onchange('precio','quantity')
    def _onchange_price(self):
        # set auto-changing field
        # self.price = self.amount * self.unit_price
        # Can optionally return a warning and domains
        self.subtotal = self.precio * self.quantity





class contrato(models.Model):
    _name = "obra_civil_2.contrato"

    name = fields.Char(string='Nombre o Titulo')
    fecha = fields.Date()
    contratista = fields.Many2one('res.partner', string='Contratista')
    contratodetalle_ids = fields.One2many('obra_civil_2.contratodetalle', 'contrato_id', string='Detalle')
    resumendetalle_ids = fields.One2many('obra_civil_2.resumendetalle', 'contrato_id', string='Detalle')

    @api.model
    def create(self, vals):
        producto = super(contrato, self).create(vals)
        # self.env['obra_civil_2.avancedetalle'].create({
        #     'product_id': 1,
        #     'quantity': 1,
        #     'contrato_id': self,
        # })
        # print('pppppp')
        # print(self.id)
        # print(self.contratodetalle_ids)
        # print(vals)
        return producto


class resumendetalle(models.Model):
    _name = "obra_civil_2.resumendetalle"

    product_id = fields.Many2one('product.product', 'Servicio')
    # unidad_de_medida = fields.Char()
    # precio = fields.Float()
    quantity = fields.Float('Cant. Contrato')
    quantity_anterior = fields.Float('Cant. Ant.')
    quantity_actual = fields.Float('Cant. Actual')
    contrato_id = fields.Many2one('obra_civil_2.contrato')

    @api.model
    def create(self, vals):
        producto = super(resumendetalle, self).create(vals)
        # self.env['obra_civil_2.resumendetalle'].create({
        #     'product_id': vals['product_id'],
        #     'quantity': vals['quantity'],
        #     'contrato_id': vals['contrato_id'],
        # })
        # print('pppppp')
        # print(self.id)
        # print(self.contrato_id)
        # print(vals)
        print('hola desde create de resumen papaaa')
        return producto


class avancedetalle(models.Model):
    _name = "obra_civil_2.avancedetalle"

    product_id = fields.Many2one('product.product', 'Servicio')
    # unidad_de_medida = fields.Char()
    # precio = fields.Float()
    quantity = fields.Float('Cant. Contrato')
    quantity_anterior = fields.Float('Cant. Ant.')
    quantity_actual = fields.Float('Cant. Actual')
    contrato_id = fields.Many2one('obra_civil_2.contrato')