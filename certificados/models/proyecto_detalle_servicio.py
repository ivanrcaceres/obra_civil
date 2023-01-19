# -*- coding: utf-8 -*-

from odoo import models, fields, api

class proyecto_detalle_servicio(models.Model):
    _name = "certificados.proyecto_detalle_servicio"

    product_id = fields.Many2one('product.template')
    unidad_de_medida = fields.Many2one('product.uom')
    price_unit = fields.Float('Precio Unitario')
    quantity = fields.Float('Cantidad')

    quantity_hechas = fields.Float('Fisico Acumulado Total', compute='compute_quantity_hechas')
    montohechos = fields.Float('Montos Acumulado Total', compute='compute_quantity_hechos_monto')

    # quantity_hechas = fields.Float('Fisico Acumulado Anterior', compute='compute_quantity_hechas')
    # montohechos = fields.Float('Montos Acumulado Anterior', compute='compute_quantity_hechos_monto')
    #
    # quantity_hechas = fields.Float('Cantidades Hechas', compute='compute_quantity_hechas')
    # montohechos = fields.Float('Montos hechos', compute='compute_quantity_hechos_monto')


    project_id = fields.Many2one('project.project')

    @api.one
    def compute_quantity_hechas(self):
        self.quantity_hechas = 1 * 10 * 2
        # self.quantity_hechas = 1*10
        a = self.env['certificados.avance'].search([('project_id', '=', self.project_id.id)])
        # serviciosquetieneelproyecto = self.env['certificados.avance'].search([('project_id', '=', self.id)])
        #
        # print (a)
        # lista = []
        suma = 0
        for b in a:
            for c in b.avance_detalle_ids:
                if self.product_id == c.product_id:
                    suma = suma + c.quantity
                    print (suma)

        self.quantity_hechas = suma

    @api.one
    def compute_quantity_hechos_monto(self):
        self.montohechos = 1 * 10
        # self.quantity_hechas = 1*10
        a = self.env['certificados.avance'].search([('project_id', '=', self.project_id.id)])
        # serviciosquetieneelproyecto = self.env['certificados.avance'].search([('project_id', '=', self.id)])
        #
        # print (a)
        # lista = []
        suma = 0
        for b in a:
            for c in b.avance_detalle_ids:
                if self.product_id == c.product_id:
                    suma = suma + c.quantity
                    print (suma)

        self.montohechos = suma * self.price_unit

