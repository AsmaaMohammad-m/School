# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'School Management',
    'version' : '1.0',
    'summary': 'School Management system',
    'sequence': 10,
    'description':'My School Management' """
Invoicing & Payments
====================
The specific and easy-to-use Invoicing system in Odoo allows you to keep track of your accounting, even when you are not an accountant. It provides an easy way to follow up on your vendors and customers.

You could use this simplified accounting in case you work with an (external) account to keep your books, and you still want to keep track of payments. This module also offers you an easy method of registering payments, without having to encode complete abstracts of account.
    """,
    'category': 'Accounting/Accounting',
    'website': 'https://www.odoo.com/app/invoicing',
    'images' : ['images/accounts.jpeg','images/bank_statement.jpeg','images/cash_register.jpeg','images/chart_of_accounts.jpeg','images/customer_invoice.jpeg','images/journal_entries.jpeg'],
    'depends' : ['product'],
    'data': [
    'security/ir.model.access.csv',
    'data/sequence.xml',
        'views/school.xml',
        'report/school_report.xml',

    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'post_init_hook': '',
    'assets': {
        'web._assets_primary_variables': [
            'account/static/src/scss/variables.scss',
        ],
        'web.assets_backend': [

        ],
        'web.assets_frontend': [

        ],
        'web.assets_tests': [
        ],
        'web.qunit_suite_tests': [

        ],
    },
    'license': 'LGPL-3',
}
