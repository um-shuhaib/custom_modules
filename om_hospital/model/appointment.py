from odoo import fields, models, api

class HospitalPatient(models.Model):
    _name="hospital.appointment"
    _inherit=['mail.thread']    #add mail in depents id manifest
    _description="appointment details"
    _rec_name='patient_id'

    reference=fields.Char(string='Reference', default='New')
    patient_id=fields.Many2one('hospital.patient',string="Patient",required=True)
    date_appointment=fields.Date(string="Date")
    note=fields.Text(string="Note")
    state=fields.Selection([
        ('draft','draft'),('confirmed','confirmed'),('ongoing','ongoing'),('done','done'),('cancelled','cancelled')
        ],default='draft')

    
    @api.model_create_multi
    def create(self, vals_list):
        print("..................",vals_list)
        for val in vals_list:
            if not val.get('reference') or val['reference'] == 'New':
                val['reference'] = self.env['ir.sequence'].next_by_code('hospital.appointment')
        return super().create(vals_list)
    
    def action_confirm(self):
        for rec in self:
            rec.state='confirmed'



