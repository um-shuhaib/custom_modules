from odoo import fields, models


class PropertyModel(models.Model):
    _name = 'property.model'

    Property_name = fields.Char(string="Property Name")
    location = fields.Char(string="Location")
    types = fields.Selection([('type1','Type 1'),('type2','Type 2'),('type3','Type 3')],string="Type")
    total_unit = fields.Integer(string="Total Unit", readonly=True , default="00")
    ownership_type = fields.Selection([('type1','Type 1'),('type2','Type 2'),('type3','Type 3')],string="Ownership Type")
    owner = fields.Char(string="Owner")
    unit_prefix = fields.Char(string="Unit Prefix")
    number_of_sequence = fields.Integer(string="Number of Sequence")
    starting_number = fields.Integer(string="Starting Number")
    country = fields.Char(string="Country")
    emirates = fields.Char(string="Emirates")
    city = fields.Char(string="City")
    street_name = fields.Char(string="Street Name")
    google_map = fields.Char(string="Google Map")
    building_no = fields.Char(string="Building Number")
    year_build = fields.Date(string="Year Build")
    total_floor = fields.Integer(string="Total Floor")
    total_parking = fields.Integer(string="Total Parking")

    number_of_gate = fields.Integer(string="Number Of Gate")
    total_area = fields.Integer(string="Total Area")
    land_area = fields.Integer(string="Land Area")
    property_market_value = fields.Integer(string="Property Market Value")
    annuel_service_charge = fields.Integer(string="Annual Service Charge")
    insurance_policy_number = fields.Integer(string="Insurence Policy Number")
    management_fees = fields.Integer(string="Management Fees")
    vat = fields.Integer(string="VAT")
    insurance_renewal_date = fields.Date(string="Insurance Renewal Date")
    electricity_number = fields.Integer(string="Electricity Number")
    water_number = fields.Integer(string="Water Number")
    gas_supply_available = fields.Char(string="Gas Supply Available")
    bank = fields.Char(string="Bank")
    bank_account = fields.Char(string="Bank Account")
    account_holder = fields.Char(string="Account Holder")

    gym = fields.Boolean(string="Gym")
    parking = fields.Boolean(string="Parking")
    access_control = fields.Boolean(string="Access Control")

    swimming_pool = fields.Boolean(string="Swimming Pool")
    security = fields.Boolean(string="Security")
    retail_area = fields.Boolean(string="Retail Area")


    kid_play_area = fields.Boolean(string="Kid Play Area")
    cctv = fields.Boolean(string="CCTV")
    park_garden = fields.Boolean(string="Park/Garden")

    rera_ejary_property_code = fields.Char(string="RERA/Ejary Property Code")
    municiple_reg_no = fields.Char(string="Municipal Reg No")
    barcode = fields.Char(string="Barcode")

    title_deed_attachment_ids = fields.Many2many("ir.attachment","title_deed_rel","rec_id","attach_id",string="Title Deed")
    site_master_plan_attachment_ids = fields.Many2many("ir.attachment","site_master_rel","rec_id","attach_id", string="Site Master Plan")
    property_layout_attachment_ids = fields.Many2many("ir.attachment","property_layout_rel","rec_id","attach_id", string="Property Layout Drawing")
    mep_drawing_attachment_ids = fields.Many2many("ir.attachment","mep_drawing_rel","rec_id","attach_id", string="MEP Drawing")
    fire_safety_attachment_ids = fields.Many2many("ir.attachment","fire_safety_rel","rec_id","attach_id", string="Fire Safety Certificate")
    insurence_attachment_ids = fields.Many2many("ir.attachment","insurence_attachment_rel","rec_id","attach_id", string="Insurence Document")
