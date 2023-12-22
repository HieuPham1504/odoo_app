from odoo import models, fields, api

class MapstarDivision(models.Model):
    _name = 'mapstar.division'
    _description = 'Mapstar Division'
    _order = 'id desc'

    destination_id = fields.Many2one('mapstar.destination', string='Mapstar Destination', required=True)
    name = fields.Char(string='Division Name', required=True)
    description = fields.Text(string='Division Description')

