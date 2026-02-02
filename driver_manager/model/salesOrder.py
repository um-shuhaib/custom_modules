from odoo import fields, models, api

class Salesorder(models.Model):
    _inherit="sale.order"

    # contact=fields.Char(string="Cus_Contact" , related="partner_id.phone")
    contact=fields.Char(string="Cus_Contact")



    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        if self.partner_id:
            self.contact=self.partner_id.phone
        