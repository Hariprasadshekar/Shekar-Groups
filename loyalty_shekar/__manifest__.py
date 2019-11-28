{
    'name': 'Loyalty rewards report ',
    'version': '12.3',
    'category': 'Tools',
    'summary': "This module consists, the customized Templates",
    'depends': ['account','shekar_custom_invoice','sale_loyalty_ae'],
    'website': 'http://www.prixgen.com',
    'data': [
             # 'views/custom_web.xml',
             'reports/testing_rewards.xml',
             'views/tax_amount.xml',
             'views/header_footer.xml',

             # 'views/rewards_report.xml',
             # 'views/loyalty_rewards_report.xml',
             ],
    'auto_install': False,
    'application': True,
}

