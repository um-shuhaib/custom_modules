from odoo import models, fields

class OwlModel(models.Model):
    _name='owl.patient'

    number=fields.Integer(string="Count" , default=0)

    