# -*- coding: utf-8 -*-
# Copyright© 2016-2017 ICTSTUDIO <http://www.ictstudio.eu>
# License: AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)
import logging

from odoo import models, fields, api, _

_logger = logging.getLogger(__name__)

class ResPartner(models.Model):
    _inherit = "res.partner"
    
    need_sync_count = fields.Integer(
        compute="compute_sync_count",
        string="To Sync Partners"
    )
    need_sync_total = fields.Integer(
            compute="compute_sync_count",
            string="Total Sync Entries"
    )

    need_sync_connections = fields.One2many(
        comodel_name="need.sync.connection",
        string="Need Sync Connections",
        compute="_get_need_sync_connection",
        inverse="_set_need_sync_connection"
    )

    @api.multi
    def _get_need_sync_connection(self):
        """
        Only show connections on Partner with model activated
        :return: 
        """
        for rec in self:
            need_sync_connection_models = rec.env['need.sync.connection.model'].search(
                [
                    ('model', '=', 'res.partner')
                ]
            )
            rec.need_sync_connections = need_sync_connection_models.mapped('need_sync_connection')

    @api.multi
    def _set_need_sync_connection(self):
        for rec in self:
            for need_sync_connection in rec.need_sync_connections:
                #need_sync_connection.set_published(rec.id, rec._model, need_sync_connection.published, 'product.product')
                _logger.debug("Nothing")

    @api.multi
    def compute_sync_count(self):
        for rec in self:
            _logger.debug("Model: %s", rec._model)
            need_sync_lines = rec.env['need.sync.line'].search(
                    [
                        ('model', '=', str(rec._model)),
                        ('res_id', '=', rec.id),
                    ]
            )
            rec.need_sync_count = len(
                    need_sync_lines.filtered(lambda b: b.sync_needed)
            )
            rec.need_sync_total = len(need_sync_lines)

    @api.multi
    def open_need_sync(self):
        assert len(self) == 1, 'This option should only be used for a single id at a time.'

        filter_domain = [
            ('res_id', '=', self.id),
            ('model', '=', 'res.partner')
        ]

        return {
            'name': _('Open Need Sync'),
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'tree,form',
            'res_model': 'need.sync.line',
            'src_model': 'res.partner',
            'target': 'current',
            'ctx': {'search_default_filter_sync_needed':1},
            'domain': filter_domain
        }

    @api.multi
    def unlink(self):
        self.env['need.sync'].unlink_records('res.partner', self.ids)
        return super(ResPartner, self).unlink()