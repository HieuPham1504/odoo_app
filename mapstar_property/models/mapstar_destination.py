from odoo import models, fields, api


class MapstarDestination(models.Model):
    _name = 'mapstar.destination'
    _description = 'Mapstar Destination'
    _order = 'id desc'

    name = fields.Char(string='Destination Name', required=True)
    description = fields.Text(string='Destination Description')
    city = fields.Char(string='Destination City')
