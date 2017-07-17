# -*- coding: utf-8 -*-
# Copyright© 2016 ICTSTUDIO <http://www.ictstudio.eu>
# License: AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

{
    'name': 'Picking Sale Order Salesteam',
    'version': '8.0.1.0.2',
    'category': 'Sales & Invoicing',
    'summary': """Sales Team on Picking related to Order
    """,
    'author': 'ICTSTUDIO, André Schenkels',
    'license': 'AGPL-3',
    'website': 'http://www.ictstudio.eu',
    'depends': [
        'stock_sale_order_stored'
    ],
    'data': [
        'views/stock_picking.xml',
    ],
}
