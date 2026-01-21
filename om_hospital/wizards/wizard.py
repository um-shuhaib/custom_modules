from odoo import fields, models

class AddPatient(models.TransientModel):
    _name='hospital.new.patient'

    name=fields.Char(string="Name")
    age=fields.Char(string="Age")
    bdate=fields.Char(string="Date of Birth")
    gender=fields.Char(string="Gender")