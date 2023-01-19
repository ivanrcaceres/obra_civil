# -*- coding: utf-8 -*-

from odoo import models, fields, api



# class Task(models.Model):
#     _inherit = "project.task"
#
#     tarearealizada_ids = fields.One2many( 'obra_civil.tarearealizada')
#
# class tarearealizada(models.Model):
#     _name = 'obra_civil.tarearealizada'
#     cantidad = fields.Float()
#     fecha = fields.Datatime()


class Task2(models.Model):
    _inherit = "project.task"

    # tarearealizada_ids = fields.One2many('obra_civil.ejecucion', 'task_id')
    # tarearealizada_ids = fields.One2many('obra_civil.ejecucion')
    tarearealizada_ids = fields.One2many('obra_civil.ejecucion', 'task_id', string="Servicio relacionados")


class Ejecucion(models.Model):
    _name = "obra_civil.ejecucion"
    product_id = fields.Many2one('product.product')
    quantity = fields.Float()
    fecha = fields.Datetime()
    task_id = fields.Many2one('project.task')



# class obra_civil(models.Model):
#     _name = 'project.task'
#
#     name = fields.Char(string='Nombre')
#     partner_id = fields.Many2one('res.partner', ondelete='cascade', string="Cliente", required=True)
#     montoanoexceder = fields.Float(string='Monto a no exceder')
#     descripcion = fields.Text()
#     proyecto_ids = fields.One2many('project.project', 'contrato_id',string="Proyectos relacionados")
#
# class proyecto(models.Model):
#     _inherit = 'project.project'
#     nombre = fields.Char(string='Nombre')
#     contrato_id = fields.Many2one('obra_civil.contrato',string="Contrato relacionado")