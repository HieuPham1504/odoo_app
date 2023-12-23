# -*- coding: utf-8 -*-
{
    'name': "mapstar_property",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/property_sequeces.xml',
        'views/views.xml',
        'views/mapstar_views.xml',
        'views/mapstar_property_views.xml',
        'views/mapstar_property_construction_views.xml',
        'views/mapstar_booking_views.xml',
        'views/mapstar_feedback_views.xml',
        'views/survey_request_views.xml',
        'views/mapstar_rating_views.xml',
        'views/mapstar_payment_views.xml',
        'views/mapstar_common_question_views.xml',
        'views/mapstar_notification_views.xml',
        'views/mapstar_notification_views.xml',
        'views/mapstar_destination_views.xml',
        'views/mapstar_division_views.xml',
        'views/mapstar_property_category_views.xml',
        'views/mapstar_housekeeper_views.xml',
        'views/res_partner_views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
}
