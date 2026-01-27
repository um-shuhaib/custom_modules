from odoo import fields, models

class HospitalPatient(models.Model):
    _name="hospital.appointment"
    _inherit=['mail.thread']    #add mail in depents id manifest
    _description="appointment details"
    _rec_name='patient_id'

    patient_id=fields.Many2one('hospital.patient',string="Patient",required=True)
    date_appointment=fields.Date(string="Date")
    note=fields.Text(string="Note")



