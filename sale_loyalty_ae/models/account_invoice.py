# -*- coding: utf-8 -*-

from odoo import api, fields, models


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.multi
    def action_invoice_open(self):
        res = super(AccountInvoice, self).action_invoice_open()
        for inv in self.filtered(lambda i: i.type == 'out_invoice'):
            p_qty_ids = []
            # r_ids = []
            total_points = 0
            for line in inv.invoice_line_ids:
                points = 0
                loyalty_lines = self.env['loyalty.program.line'].search([('product_id', '=', line.product_id.id)])
                # lerpq = self.env['loyalty.earning.report.product.qty'].create({'product_id': line.product_id.id, 'qty': line.quantity})
                for lline in loyalty_lines:
                    now = fields.Datetime.now() 
                    if lline.program_id.start_date <= now <= lline.program_id.end_date:
                        points += lline.points * line.quantity
                total_points += points
                        # p_qty_ids.append(lerpq.id)
                self.env['loyalty.earning.report'].create({
                        'invoice_id': inv.id,
                        'partner_id': inv.partner_id.id,
                        'product_id': line.product_id.id,
                        'qty': line.quantity,
                        'points': points,
                        # 'product_ids': [(6, 0, p_qty_ids)],
                })
                # r_ids.append(r_id)
            # self.env['loyalty.earning.report'].browse(r_ids).write({'points': points})
            total_points += inv.partner_id.loyalty_points
            inv.partner_id.write({'loyalty_points': total_points})
            print(">>>>>>>>>>>>>>>>>>>> inv name", inv.name)
        return res