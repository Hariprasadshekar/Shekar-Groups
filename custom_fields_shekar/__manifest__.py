{
    'name': 'Addon Fields',
    'version': '1.0',
    'category': 'Tools',
    'summary': "Module for customized fields.",
    'depends': ['base','hr','sale_management','purchase','crm','account','sale','product'],
    'author': 'Prixgen Tech Solutions Pvt. Ltd.',
    'company': 'Prixgen Tech Solutions Pvt. Ltd.',
    'website': 'https://www.prixgen.com',
    'data': ['views/account_invoice.xml',
              'views/crm_lead.xml',
              'views/custom_fields.xml',
              'views/hr_employee.xml',
              'views/purchase_order.xml',
              'views/res_company.xml',
              'views/res_partner.xml',
              'views/sale_order.xml',
              'views/emp_details.xml',
              'views/sales_order_line.xml',
              'views/sale_order_view1.xml',
              'views/purchase_order_view1.xml',
             ],
    'auto_install': False,
    'application': True,
}