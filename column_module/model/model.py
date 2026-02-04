from odoo import fields, models


class ColumnModel(models.Model):
    _name = 'column.model'

    name = fields.Char(string="Name")
    name1 = fields.Char(string="Name1")
    name2 = fields.Char(string="Name2")
    name3 = fields.Char(string="Name3")
    name4 = fields.Char(string="Name4")
    name5 = fields.Char(string="Name5")