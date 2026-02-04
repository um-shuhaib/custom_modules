from odoo import fields, models

class AddPatient(models.TransientModel):
    _name='sales.xlsx.wizard'

    start_date = fields.Date(string="Start Date",required=True)
    end_date = fields.Date(string="End Date",required=True)


    