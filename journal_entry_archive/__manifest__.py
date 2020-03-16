# Copyright 2017-2018 Onestein (<https://www.onestein.eu>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    'name': 'Journal Entry Archive',
    'summary': 'Archive Journal Entries',
    'author': 'Onestein, Odoo Community Association (OCA)',
    'website': 'https://github.com/OCA/purchase-workflow',
    'category': 'Journal Entries',
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    'depends': [
        'account_accountant',
    ],
    'data': [
        'views/account_move.xml',
    ],
    'installable': True,
}
