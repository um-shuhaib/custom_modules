from odoo import fields, models

class UnitModel(models.Model):
    _name = 'unit.model'
    _rec_name = 'unit_code'

    property_id = fields.Many2one('property.model',string="Property Name")
    block_id = fields.Many2one('block.model',string="Block")
    unit_subtype_id = fields.Many2one('res.partner',string="Unit Subtype")
    unit_code = fields.Char(string="Unit Code", readonly=True, default="LT-001")
    floor = fields.Selection([('1','1'),('2','2'),('3','')], string="Floor")
    furnishing_status = fields.Selection([('furnished','Furnished'),('not_furnished','Not Furnished')],string="Furnishing Status")
    unit_number = fields.Integer(string="Unit Number")
    unit_type_id = fields.Many2one('res.partner',string="Unit Type")
    under_maintenence = fields.Boolean(string="Under Maintenence")

    unit_size_sq_sq_ft = fields.Integer(string="Unit Size Sq.Sq.Ft")
    monthly_rent = fields.Integer(string="Monthly Rent")
    unit_size_sq_sq_mt = fields.Integer(string="Unit Size Sq.Sq.Mt", readonly=True, default="88")
    minimum_rent = fields.Integer(string="Minimum Rent")
    annuel_rent = fields.Integer(string="Annuel Rent")
    total_parking = fields.Integer(string="Total Parking")

    number_of_bedroom = fields.Integer(string="Number of Bed Room")
    facing_direction = fields.Selection([('west','West'),('north','North')],string="Facing Direction")
    number_of_bathroom = fields.Integer(string="Number of Bath Room")
    number_of_free_parking = fields.Integer(string="Number of Free Parking")
    balcony = fields.Integer(string="Balcony")
    parking_slot = fields.Selection([('101','101'),('102','102')],string="Parking Slot")

    gym = fields.Boolean(string="Gym")
    parking = fields.Boolean(string="Parking")
    access_control = fields.Boolean(string="Access Control")
    document_ids = fields.Many2many('ir.attachment','document_ids_rel','rec_id','attach_id',string="Document")
    document2_ids = fields.Many2many('ir.attachment','document2_ids_rel','rec_id','attach_id',string="Document 2")
    swimming_pool = fields.Boolean(string="Swimming Pool")
    security = fields.Boolean(string="Security")
    retail_area = fields.Boolean(string="Retail Area")
    expiry_date = fields.Date(string="Expiry Date")
    expiry_date2 = fields.Date(string="Expiry Date")

    kid_play_area = fields.Boolean(string="Kid Play Area")
    cctv = fields.Boolean(string="CCTV")
    park_garden = fields.Boolean(string="Park/Garden")


