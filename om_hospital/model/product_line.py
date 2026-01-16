from odoo import fields, models

class ProductLines(models.Model):
    _name="product.line"
    _description="products can select from here"

    patient_id=fields.Many2one('hospital.patient',string="Patient")
    product_id=fields.Many2one('product.product',string="Product",required=True)
    quantity=fields.Float(string="Quantity",default=1.0)

