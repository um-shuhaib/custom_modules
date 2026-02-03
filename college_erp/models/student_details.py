from odoo import fields,models

class StudentDetails(models.Model):
    _name = 'student.details'

    name = fields.Char(string="Name")
    place = fields.Char(string="Place")
    