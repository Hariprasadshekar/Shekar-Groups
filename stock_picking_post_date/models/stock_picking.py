# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    post_date = fields.Datetime('Post Date', copy=False)

    @api.multi
    def action_done(self):
        res = super(StockPicking, self).action_done()
        for picking in self:
            if picking.post_date:
                self.write({'date_done': picking.post_date})
        return res

