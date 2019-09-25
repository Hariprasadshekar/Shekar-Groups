# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    loyalty_points = fields.Float(string="Loyalty Points", copy=False)
