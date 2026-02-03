from odoo import fields, models

class StudentModel(models.Model):
    _name = 'student.student'
    _description = 'Student Details'
    _inherit = ['mail.thread','mail.activity.mixin']

    student_id = fields.Many2one(comodel_name='student.details',string="Student" , required=True, tracking=True)
    subject = fields.Selection(selection=[('math',"Mathematics"),('sci','Science'),('eng','English')],string='Subject', required=True, tracking=True)
    date = fields.Date(string="Date of Exam", required=True,tracking=True)
    status = fields.Selection([('pass','Pass'),('fail','Fail')],string='Status',required=True, tracking=True)
    mark = fields.Integer(string="Mark", required=True, tracking=True)

