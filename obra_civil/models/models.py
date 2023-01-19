# -*- coding: utf-8 -*-

from odoo import models, fields, api
# from . import project

# class obra_civil(models.Model):
#     _name = 'obra_civil.obra_civil'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class obra_civil(models.Model):
    _name = 'obra_civil.contrato'

    name = fields.Char(string='Nombre')
    partner_id = fields.Many2one('res.partner', ondelete='cascade', string="Cliente", required=True)
    montoanoexceder = fields.Float(string='Monto a no exceder')
    descripcion = fields.Text()
    proyecto_ids = fields.One2many('project.project', 'contrato_id',string="Proyectos relacionados")

class proyecto(models.Model):
    _inherit = 'project.project'
    nombre = fields.Char(string='Nombre')
    contrato_id = fields.Many2one('obra_civil.contrato',string="Contrato relacionado")
    venta_id = fields.Many2one('sale.order')

    # heredar xml

class pedidodemateriales(models.Model):
    _inherit = 'purchase.order'

    tarea_id = fields.Many2one('project.task', string="tarea relacionado")

class tarea(models.Model):
    _inherit = 'project.task'

    pedido_ids = fields.One2many('purchase.order', 'tarea_id', string="Pedidos relacionados")






# class proyecto_obra_civil(models.Model):
#     _name = 'obra_civil.proyectoobra'
#
#     contrato = fields.Many2one('obra_civil.contrato', ondelete='cascade', string="Contrato", required=True)
#     nombre = fields.Char(string='Nombre')
#     fechadeinicio = fields.Date()
#     fechadefinalizacion = fields.Date()
#     fechadeinicio_tentativo = fields.Date()
#     fechadefinalizacion_tentativo = fields.Date()
#     costo_tentativo = fields.Float()
#     costo_real = fields.Float()
#     tarea_ids = fields.One2many('obra_civil.tarea')
#
# class tarea(models.Model):
#     _name = 'obra_civil.tarea'
#
#     nombre = fields.Char(string='Nombre')
#     descripcion = fields.Char(string='Descripcion')
#     prioridad = fields.Selection([
#         ('alta', 'Alta'),
#         ('media', 'Media'),
#         ('baja', 'Baja'),
#     ])
#     estado = fields.Selection([
#         ('planeado', 'Planeado'),
#         ('endesarrollo', 'En desarrollo'),
#         ('finalizado', 'Finalizado'),
#     ])

###########################################################  aqui abajo la clase tarea nueva
class tarea2(models.Model):
    _inherit = 'project.task'

    producto_id = fields.Many2one('product.product', string="Servicio relacionado")
    descripcion = fields.Char(string='Descripcion')