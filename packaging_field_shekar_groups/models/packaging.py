from odoo import fields, models,api,_
from odoo.exceptions import UserError, ValidationError
from odoo.tools.float_utils import float_compare, float_is_zero, float_round

class Packagingsales(models.Model):
    _inherit='sale.order.line'

    z_no_of_package = fields.Float(string='No of Package',default=0.0,compute="_get_package_name_no_packages")
    z_package = fields.Char(string="Package",compute="_get_package_name_no_packages")
    z_scheme = fields.Char(string="Scheme",compute="_get_loyalty_name")

    @api.depends('product_id', 'name')
    def _get_package_name_no_packages(self):
        for line in self:
            pack = self.env['product.packaging'].search([('product_id','=',line.product_id.id)])
            for pack_name in pack:
                line.z_package = pack_name.name        
                line.z_no_of_package = line.product_uom_qty/pack_name.qty

    @api.depends('product_id', 'name')
    def _get_loyalty_name(self):
        for line in self:
            loyalty_rec = self.env['loyalty.program.line'].search([('product_id','=',line.product_id.id)])
            for loyalty_name in loyalty_rec:
                line.z_scheme = loyalty_name.program_id.name        
                

class Packaginginvoice(models.Model):
    _inherit='account.invoice.line'

    zi_no_of_package = fields.Float(string='No of Package',default=0.0,compute="_get_package_name_no_packages_invoice")
    zi_package = fields.Char(string="Package",compute="_get_package_name_no_packages_invoice")
    zi_scheme = fields.Char(string="Scheme",compute="_get_loyalty_name_invoice")

    @api.depends('product_id', 'name')
    def _get_package_name_no_packages_invoice(self):
        for line in self:
            pack = self.env['product.packaging'].search([('product_id','=',line.product_id.id)])
            for pack_name in pack:
                line.zi_package = pack_name.name        
                line.zi_no_of_package = line.quantity/pack_name.qty
    
    @api.depends('product_id', 'name')
    def _get_loyalty_name_invoice(self):
        for line in self:
            loyalty_rec = self.env['loyalty.program.line'].search([('product_id','=',line.product_id.id)])
            for loyalty_name in loyalty_rec:
                line.zi_scheme = loyalty_name.program_id.name 