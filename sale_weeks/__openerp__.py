# -*- encoding: utf-8 -*-
##############################################################################
#
#    Sale Quotation Weeks
#
#    Copyright (C) 2015 ICTSTUDIO (<http://www.ictstudio.eu>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Sale Quotation Weeks',
    'version': '0.1',
    'depends': ['sale'],
    'author': "ICTSTUDIO, André Schenkels",

    'website': 'http://www.ictstudio.eu',
    'category': 'Sales Management',
    'sequence': 100,
    'data': [
        'sale_view.xml',
        'views/report_sale_order.xml',
    ],
}
