from odoo import api, fields, models
import datetime

class HospitalPatient(models.Model):
    _name="hospital.patient"
    _inherit=['mail.thread']    #add mail in depents id manifest
    _description="Patient Master"
    _rec_name='name'

    name=fields.Char(string="Name",required=True , tracking=True)
    date_of_birth=fields.Date(string="Date Of Birth",required=True)
    gender=fields.Selection([('male','male'),('female','female')],string="Gender")
    age=fields.Char(string="Age",compute="_get_patient_age")
    product_ids=fields.One2many('product.line','patient_id',string="product")
    company_id=fields.Many2one('res.company',string="Company",required=True,default=lambda self: self.env.company)
    # Other patient field)
    @api.depends('date_of_birth')
    def _get_patient_age(self):
        today=datetime.date.today()
        for patient in self:
            if patient.date_of_birth:
                bdate=fields.Datetime.to_datetime(patient.date_of_birth).date()
                age=str(int((today-bdate).days/365))        
                patient.age=age
            else:
                patient.age="not provided"

    def action_newPatient(self):
        action_ref = self.env.ref('om_hospital.wizard_addPatient_action').read()[0]
        return action_ref