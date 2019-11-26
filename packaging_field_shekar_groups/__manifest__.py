# -*- coding: utf-8 -*-
{
    'name': "Packaging field with number of package with scheme field",

    'category': 'Test',
    'version': '12.0.1',
    'description': """Packging field in Quotation  with number of package with scheme field,sale order and accounting""",
    # any module necessary for this one to work correctly
    'depends': ['base','account','crm','sale',],

    # always loaded
    'data': [
             'views/packaging_view.xml',
    ],
}
