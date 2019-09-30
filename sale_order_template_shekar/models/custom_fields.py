from odoo.exceptions import UserError
from odoo import api, fields, models, _

class Partner(models.Model):
    _inherit = "res.partner"


    pan_num = fields.Char(string='PAN', store=True)


class Bank(models.Model):
    _inherit = 'res.bank'

    account_type = fields.Char( string='Account Type' , stre=True)