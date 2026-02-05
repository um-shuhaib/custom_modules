from odoo import fields, models


class BlockModel(models.Model):
    _name = 'block.model'
    _rec_name = 'block_name'

    block_name = fields.Char(string="Block Name")
    property_id = fields.Many2one('property.model',string="Property Name")
    user_id = fields.Many2one('res.partner',string="User")
    company_id = fields.Many2one('res.partner',string="Company")