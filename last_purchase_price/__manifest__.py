# -*- coding: utf-8 -*-
{
    'name': "Last Purchase Price",

    'summary': """
        Adds a last purchase cost and last purchase date to a product""",

    'description': """
        Adds a last purchase cost and last purchase date to a product
    """,

    'author': "Indasoge SpA",
    'website': "http://www.indasoge.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales/Sales',
    'version': '15.0.1.0.5',

    # any module necessary for this one to work correctly
    'depends': ['product'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/product_views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
