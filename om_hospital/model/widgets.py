from odoo import fields, models

class forWidgets(models.Model):
    _name='patient.widget'
    _description="model is created for applying widgets"
    _rec_name='name'

    name=fields.Char(string="Name")
    address=fields.Text(string="address" ,default='you can copy me')
    age=fields.Integer(string="Age")
    decimal=fields.Float(string="Progression")
    Date=fields.Date(string="Date")
    DateTime=fields.Datetime(string="Date and Time")
    status=fields.Boolean(string="Status")
    stage=fields.Selection([('good','good'),('bad','bad'),('wow','wow')],string="stage")
    pdf=fields.Binary(string='uploads')


