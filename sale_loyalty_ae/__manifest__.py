# -*- coding: utf-8 -*-
{
    'name': 'Sale Loyalty Program',
    'version': '12.0.1.0.0',
    'author': 'Ascents Entrepreneurs',
    'license': 'OPL-1',
    'category': 'sale',
    'summary': 'Loyalty Program for Sale',
    'description': """
Loyalty Program for Sale
-------------------------

Loyalty Program for Sale
""",
    'depends': ['sale'],
    'data': [
        'data/redemption_sequence.xml',
        'security/ir.model.access.csv',
        'views/loyalty_program_views.xml',
        'wizard/redemption_wizard.xml',
    ],
    'installable': True,
    'auto_install': False,
    'currency': 'EUR',
    'price': 20,
}
