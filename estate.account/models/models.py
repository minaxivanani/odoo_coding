# -*- coding: utf-8 -*-

from odoo import models, fields, api


class EstateProperty(models.Model):
	_inherit = "estate.property"

	def action_sold(self):
        # print("\n\n In action sold")
        for record in self:
            vals = {}
            journal = self.env['account.move'].with_context(default_move_type='out_invoice')._get_default_journal()
            vals ['partner_id'] = record.buyer_id.buyer_id
            vals ['move_type'] = "out invoice"
            vals ['journal_id'] = journal.id
            vals ['invoice_line_ids'] = [(0,0,{'name':record.name,'quantity':1,'price_unit':'record.selling_price'})]
            self.env('account move').create(vals)
            # return some action  

	


# class estate.account(models.Model):
#     _name = 'estate.account.estate.account'
#     _description = 'estate.account.estate.account'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
