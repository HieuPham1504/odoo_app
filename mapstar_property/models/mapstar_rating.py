from odoo import models, fields, api

class MapstarRating(models.Model):
    _name = 'mapstar.rating'
    _description = 'Mapstar Rating'
    _order = 'id desc'

    property_id = fields.Many2one('mapstar.property', string='Mapstar Property', required=True)
    customer_name = fields.Char(string='Customer Name', required=True)
    rating = fields.Selection([
        ('0', 0),
        ('1', 1),
        ('2', 2),
        ('3', 3),
        ('4', 4),
        ('5', 5),
    ], default='5', string='Rating')
    date = fields.Datetime(string='Rating Date', required=True)
    description = fields.Text(string='Rating Description')
