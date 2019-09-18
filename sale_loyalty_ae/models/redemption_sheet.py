# -*- coding: utf-8 -*-

from odoo import api, fields, models


class RedemptionSheet(models.TransientModel):
    _name = 'redemption.sheet'
    _description = 'Redemption Sheet'

    partner_id = fields.Many2one('res.partner', string='Customer', domain=[('customer', '=', True)])
    points = fields.Float(string="Total Points")
    redemption_value = fields.Float(string="Redemption Value")
    sequence = fields.Char(string='Ref. No', default=lambda self: self.env['ir.sequence'].next_by_code('redemption.sheet'))


