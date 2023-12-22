from odoo import models, fields, api

class ResUsersInherited(models.Model):
    _inherit = "res.users"

    show_demo_land = fields.Boolean(string='Show Demo Land', default=False)