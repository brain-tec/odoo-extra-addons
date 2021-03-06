# -*- encoding: utf-8 -*-
##############################################################################
#
#    Item number
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

from openerp import models, fields, api, _
import logging
_logger = logging.getLogger(__name__)

class stock_move(models.Model):
    _inherit = 'stock.move'
    _order = 'item_number'
    item_number = fields.Char(string='Item Number')

    def _get_invoice_line_vals(self, cr, uid, move, partner, inv_type, context=None):
        '''Add Item Number to the invoice vals for correct invoicing'''
        res = super(stock_move, self)._get_invoice_line_vals(cr, uid, move, partner, inv_type, context=context)
        res['item_number'] = move.item_number or 0
        return res