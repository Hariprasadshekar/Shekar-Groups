{
    'name': 'TDS Calculation',
    'version': '1.0.1',
    'category': 'TDS',
    'summary': 'TDS Functionality',
    'author': 'Prixgen Tech Solutions Pvt Ltd.',
    'company': 'Prixgen Tech Solutions Pvt Ltd.',
    'website': 'https://www.prixgen.com',
    'depends': ['stock','product','purchase','account'],
    'data': [
        'views/tds_group_settings_view.xml',
        'views/tds_mapping.xml',
        'views/tds_group.xml',
        'views/tds_section.xml',
        'views/assesse_code.xml',
        'views/concession_code.xml',
        'views/tds_nod.xml',
        'views/nod_configuration.xml',
        'views/account_invoice.xml',

        'views/res_partner.xml',
        'views/purchase.xml'
    ],
    'installable': True,
    'auto_install': False,
}
