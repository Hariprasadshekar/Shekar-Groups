# -*- coding: utf-8 -*-

from odoo import api, fields, models


class LoyaltyProgram(models.Model):
    _name = 'loyalty.program'
    _description = 'Loyalty Program'

    name = fields.Char(required=True)
    start_date = fields.Datetime(string="Start Date", required=True)
    end_date = fields.Datetime(string="End Date", required=True)
    program_lines = fields.One2many('loyalty.program.line', 'program_id', string='Loyalty Program Lines')

    _sql_constraints = [
        ('date_check', "CHECK ( (start_date <= end_date))", "The start date must be anterior to the end date.")
    ]


class LoyaltyProgramLine(models.Model):
    _name = 'loyalty.program.line'
    _description = 'Loyalty Program Line'

    program_id = fields.Many2one('loyalty.program')
    product_id = fields.Many2one('product.product', string='Product', required=True, domain=[('sale_ok', '=', True)], change_default=True, ondelete='restrict')
    category_id = fields.Many2one('product.category', 'Category')
    points = fields.Float(string="Points per Quantity")


class LoyaltyPointsCockpit(models.Model):
    _name = 'loyalty.points.value.cockpit'
    _description = 'Loyalty Points Value Cockpit'

    name = fields.Char(string="Offer Name", required=True)
    start_date = fields.Date(string="Start Date", required=True)
    end_date = fields.Date(string="End Date", required=True)
    cockpit_line = fields.One2many('loyalty.points.value.cockpit.line', 'cockpit_id', string='Cockpit Lines')


class LoyaltyPointsCockpitLine(models.Model):
    _name = 'loyalty.points.value.cockpit.line'
    _description = 'Loyalty Points Value Cockpit Line'

    cockpit_id = fields.Many2one('loyalty.points.value.cockpit')
    cockpit_type = fields.Char(string="Type", required=True)
    min_points = fields.Float(string="Min Quantity", required=True)
    max_points = fields.Float(string="Max Quantity", required=True)
    value = fields.Float(string="Value", required=True)


class LoyaltyEarningReport(models.Model):
    _name = 'loyalty.earning.report'
    _description = 'Loyalty Earning Report'

    invoice_id = fields.Many2one('account.invoice')
    invoice_date = fields.Date(related="invoice_id.date_invoice")
    inv_number = fields.Char(related="invoice_id.number", string="Invoice Number")
    # product_ids = fields.Many2many('loyalty.earning.report.product.qty', string='Products and Quantity')
    partner_id = fields.Many2one('res.partner', string='Customer', domain=[('customer', '=', True)])
    product_id = fields.Many2one('product.product', string='Product', domain=[('sale_ok', '=', True)])
    qty = fields.Float(string="Product Quantity")
    points = fields.Float(string="Reward Points")
    status = fields.Selection([('open', 'Open'), ('redeemed', 'Redeemed')], default="open")


class LoyaltyEarningReport(models.Model):
    _name = 'loyalty.earning.report.product.qty'
    _description = 'Loyalty Earning Report Product:Quantity'

    product_id = fields.Many2one('product.product', string='Product', domain=[('sale_ok', '=', True)])
    qty = fields.Float(string="Product Quantity")

    @api.multi
    def name_get(self):
        return [(value.id, "%s: %s" % (value.product_id.name, value.qty)) for value in self]