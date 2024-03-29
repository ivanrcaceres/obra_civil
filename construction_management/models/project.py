# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from openerp import models, fields, api, _
import openerp.addons.decimal_precision as dp


class project_project(models.Model):
    _inherit = 'project.project'

    @api.multi
    def _find_cost(self):
        bill_qty_obj = self.env['bill.quantity']
        bill_qty_search = bill_qty_obj.search([])
        for record in bill_qty_search:
            if record.project_id.id == self.id:
                self.project_cost = record.material_cost + record.labor_cost + record.subcontract_cost + record.equipment_cost + record.work_package_cost + self.project_cost 
        return True      

        
    @api.multi
    def _find_line_usage(self):
        bill_qty_line_obj = self.env['bill.quantity.line']
        bill_qty_line_search = bill_qty_line_obj.search([])
        for line in bill_qty_line_search:
            if line.bill_quantity_id.project_id.id == self.id:
                if line.key=='material' and line.product_id:
                    vals = {
                        'product_id':line.product_id.id,
                        'uom_id':line.uom_id.id,
                        'qty':line.qty,
                        'price_unit':line.price_unit,
                        'price_subtotal':line.price_subtotal,
                        'project_id':line.bill_quantity_id.project_id.id
                        }
                    self.inventory_usages_ids |= self.env['product.product.extension'].create(vals)
                if line.key=='work_package' and line.work_package_id:
                    vals = {
                        'work_package_id':line.work_package_id.id,
                        'uom_id':line.uom_id.id,
                        'qty':line.qty,
                        'price_unit':line.price_unit,
                        'price_subtotal':line.price_subtotal,
                        'project_id':line.bill_quantity_id.project_id.id
                        }
                    self.work_package_ids |= self.env['work.package.extension'].create(vals)
            

        return True

    sale_order_ids = fields.Many2many("sale.order",string="Sale Order Reference")
    purchase_order_ids = fields.Many2many("purchase.order",string="Purchase Order Reference" )
    work_package_ids = fields.One2many("work.package.extension",'project_id',string="Work Package Reference", compute="_find_line_usage" )
    inventory_usages_ids = fields.One2many("product.product.extension",'project_id',string="Inventory Usage Reference", compute="_find_line_usage")
    project_deliverables_ids = fields.One2many('material.line','project_id', string='Deliverable' )
    project_cost = fields.Float(string="Project Cost", compute="_find_cost" )



class material_line(models.Model):
    _name = "material.line"

    project_id = fields.Many2one('project.project','Material')
    product_id = fields.Many2one('product.product','Products')
    planned_qty = fields.Integer( 'Planned Qty.')
    used_qty = fields.Float('Used Qty')
    status = fields.Selection([('close', 'Close'), ('open', 'Open')], "State", default="open")         
         


class work_package_extension(models.Model):
    _name = 'work.package.extension'
    
    project_id = fields.Many2one('project.project','Project')
    work_package_id = fields.Many2one('work.package','Work Package')
    uom_id = fields.Many2one('product.uom','Product UOM')
    qty = fields.Float('QTY')
    price_unit = fields.Float('Price Unit')
    price_subtotal = fields.Float('Price Subtotal')




class project_deliverables(models.Model):
    _name = 'project.deliverables'
    project_id = fields.Many2one('project.project','Project')
    
class product_product_extension(models.Model):
    _name = 'product.product.extension'

    project_id = fields.Many2one('project.project','Project')
    product_id =fields.Many2one('product.product','Product')
    uom_id = fields.Many2one('product.uom','Product UOM')
    qty = fields.Float('QTY')
    price_unit = fields.Float('Price Unit')
    price_subtotal = fields.Float('Price Subtotal')
    
    
    
    
    
