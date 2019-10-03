{
    'name': 'sale template for Shekar groups',
    'version': '12.0.0.4',
    'description': """This module consists, the customized sale Templates""",
    'category': 'Localization',
    'author': 'Prixgen Tech Solutions Pvt Ltd.',
    'company': 'Prixgen Tech Solutions Pvt Ltd.',
    'website': 'https://www.prixgen.com',
    'depends': ['sale','l10n_in_sale','web','base'],
    'data': [

        # 'views/report_sale_order.xml',
        # 'views/invisible_header.xml',
        'views/custom_fields.xml',
          'views/header_footer.xml',
        'reports/sale_report_custom.xml',
        'views/header_footer.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': True,
}
