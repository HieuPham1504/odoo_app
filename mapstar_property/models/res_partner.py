from odoo import models, fields, api

class ResPartnerInherited(models.Model):
    _inherit = "res.partner"

    res_partner_type = fields.Selection([
        ('owner', 'Owner'),
        ('customer', 'Customer'),
    ], default='customer', string='Partner Type')
    show_demo_property = fields.Boolean(string='Show Demo Property', default=False)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], default='male', string='Partner Gender')
    birthday = fields.Date(string='Partner Birthday')
