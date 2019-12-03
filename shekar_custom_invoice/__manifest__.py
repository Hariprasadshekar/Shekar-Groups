{
    'name': 'Invoice report Template Shekar',
    'version': '12.1.0.5',
    'description': """This module consists, the customized invoice Templates""",
    'category': 'Localization',
    'author': 'Prixgen Tech Solutions Pvt Ltd.',
    'company': 'Prixgen Tech Solutions Pvt Ltd.',
    'website': 'https://www.prixgen.com',
    'depends': ['account','l10n_in','web','base','product','custom_fields_shekar','customer_vendor_product_assets_number'],
    'data': [
          'views/tax_amount.xml',

        'reports/invoice_report.xml',
        'views/header_footer.xml',

        
        
    ],
    'installable': True,
    'application': False,
    'auto_install': True,
}
