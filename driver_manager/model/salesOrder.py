from odoo import fields, models

class Salesorder(models.Model):
    _inherit="sale.order"

    contact=fields.Char(string="Cus_Contact" , related="partner_id.phone")