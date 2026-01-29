from odoo import fields, models

class TodoModel(models.Model):
    _name="todo.details"

    name=fields.Char(string="Name")