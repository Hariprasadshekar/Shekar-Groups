# -*- coding: utf-8 -*-

from datetime import timedelta

from odoo import api, fields, models, _


class RedemptionSheet(models.TransientModel):
    _name = 'redemption.sheet.wizard'
    _description = 'Redemption Sheet Wizard'

    start_date = fields.Date(string="Start Date", required=True)
    end_date = fields.Date(string="End Date", required=True)
    partner_id = fields.Many2one('res.partner', string='Customer', domain=[('customer', '=', True)], required=True)

    def generate_sheet(self):
        value = 0
        for c in self.env['loyalty.points.value.cockpit'].search([]):
            if self.start_date  <= c.start_date and self.end_date >= c.end_date and c.end_date >= self.start_date:
                for line in c.cockpit_line:
                    if self.partner_id.loyalty_points >= line.min_points and  self.partner_id.loyalty_points <= line.max_points:
                        value = line.value
        self.env['redemption.sheet'].create({
            'partner_id': self.partner_id.id,
            'points': self.partner_id.loyalty_points,
            'redemption_value': value,
            })
            # 'redemption_value': self.partner_id.loyalty_points * value,
        self.env['loyalty.earning.report'].search([('partner_id', '=', self.partner_id.id)]).write({'status': 'redeemed'})
        self.partner_id.loyalty_points = 0

        view_id = self.env.ref('sale_loyalty_ae.view_redemption_sheet_tree').id
        return {
            'name':_("Redemption Sheet"),
            'view_mode': 'tree',
            'views': [[view_id, 'tree']],
            'res_model': 'redemption.sheet',
            'type': 'ir.actions.act_window',
            'target': 'current',
        }

    def view_sheet(self):
        view_id = self.env.ref('sale_loyalty_ae.view_redemption_sheet_tree').id
        return {
            'name':_("Redemption Sheet"),
            'view_mode': 'tree',
            'views': [[view_id, 'tree']],
            'res_model': 'redemption.sheet',
            'type': 'ir.actions.act_window',
            'target': 'current',
        }
