# -*- coding: utf-8 -*-

from odoo import models, fields, api


class avance(models.Model):
    _name = "certificados.avance"

    state = fields.Selection([('borrador', 'Borrador'), ('aprobado', 'Aprobado')], 'Estado', default='borrador')
    fecha_de_mediciones = fields.Date(string='Fecha de medicion')
    # quincena_id = fields.Many2one('certificados.quincena')
    lugar_id = fields.Many2one('certificados.lugar')
    project_id = fields.Many2one('project.project')

    avance_detalle_ids = fields.One2many('certificados.avance_detalle', 'avance_id', string='Avances Detalles')
    wizard_reporte_certificado_proyecto_ids = fields.Many2many('certificados.wizard_reporte_certificado_proyecto', 'avance_ids', string='Avances Finales')
    wizard_reporte_certificado_cliente_ids = fields.Many2many('certificados.wizard_reporte_certificado_cliente',
                                                               'avance_ids', string='Avances Finales')

    # avance_ids = fields.Many2many('certificados.avance', 'wizard_reporte_certificado_proyecto_ids',
    #                               string='Avances Finales')

    # @api.onchange('lugar_id')
    # def _onchange_lugar(self):
        # set auto-changing field
        # self.unidad_de_medida = self.product_id.product_tmpl_id.uom_id
        # print ('hola')

    @api.multi
    def validar(self):
        self.state = 'aprobado'

    @api.multi
    def desvalidar(self):
        self.state = 'borrador'