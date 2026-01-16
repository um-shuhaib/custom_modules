from odoo import fields, models, api
import datetime


class DriversDetails(models.Model):
    _name="driver.user"

    _description="Drivers full details"

    name=fields.Char(string="Name",required=True)
    place=fields.Char(string="Place")
    age=fields.Char(string="Age",compute="_get_user_age",required=True)
    address=fields.Text(string="Address")
    email=fields.Char(string="Email Id")
    phone=fields.Integer(string="Phone")
    vehicle_no=fields.Char(string="Vehicle No")
    licence_no=fields.Char(string="Licence No")
    bdate=fields.Date(string="Date Of Birth")
    Gender=fields.Selection([("male","male"),("female","female")],string="Gender")
    height=fields.Float(string="Height")
    single=fields.Boolean(string="Single",default=True)
    joined=fields.Datetime(string="Joined date and time")
    resume=fields.Binary(string="upload the binary")

    @api.depends('bdate')
    def _get_user_age(self):
        today=datetime.date.today()
        for driver in self:
            if driver.bdate:
                bdate=fields.Datetime.to_datetime(driver.bdate).date()
                age=str(int((today-bdate).days/365))        
                driver.age=age
            else:
                driver.age="not provided"

    