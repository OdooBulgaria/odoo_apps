# -*- coding: utf-8 -*-
# noinspection PyStatementEffect
{
    'name': 'RFID Access Control',
    'version': '0.1',
    'category': 'Human Resources',
    'summary': 'Manage employee access control',
    'author': 'Polimex',
    'license': 'GPL-3',

    'description': """\
       Description
       """,

    'website': 'securitybulgaria.com',

    'depends': [ 'base', 'hr' ],

    'data': [
        'security/hr_rfid_security.xml',
        'security/ir.model.access.csv',
        'data/hr_rfid_actions.xml',
        'data/hr_rfid_card_type_data.xml',
        'data/hr_rfid_cron_jobs.xml',
        'data/hr_rfid_time_schedule_data.xml',
        'views/hr_department_views.xml',
        'views/hr_employee_views.xml',
        'views/hr_rfid_access_group_views.xml',
        'views/hr_rfid_card_views.xml',
        'views/hr_rfid_webstack_views.xml',
    ],

    'demo': [ ],

    'installable': True,
    'auto_install': False,
}
