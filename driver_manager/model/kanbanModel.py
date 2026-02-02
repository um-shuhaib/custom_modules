from odoo import fields, models

class PatientKanban(models.Model):
    _name="test.kanban"
    _description="Created for Kanban View"

    name=fields.Char(string="Name")
    description=fields.Text(string="Description")
    date_order=fields.Date(string="Date")
    state=fields.Selection([('draft','Draft'),('in-progress','In-Progress'),('done','Done')],string="State",default="draft")
    activity_state=fields.Selection([('overdue','Overdue'),('today','Today'),('planned','Planned')],string="Activity")

