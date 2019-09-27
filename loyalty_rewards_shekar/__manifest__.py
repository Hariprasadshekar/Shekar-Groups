{
    'name': 'Loyalty rewards report ',
    'version': '12.2',
    'category': 'Tools',
    'summary': "This module consists, the customized Templates",
    'depends': ['account','shekar_agencies_invoices','sale_loyalty_ae'],
    'website': 'http://www.prixgen.com',
    'data': [
             # 'views/report_invoice_document_inherit.xml',
             'views/tax_amount.xml',
             'views/rewards_report.xml',
             'views/loyalty_rewards_report.xml',
             ],
    'auto_install': False,
    'application': True,
}
