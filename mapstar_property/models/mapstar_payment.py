from odoo import models, fields, api


class MapstarPayment(models.Model):
    _name = 'mapstar.payment'
    _description = 'Mapstar Payment'
    _order = 'id desc'

    name = fields.Char(string='Payment Name')
    payment_type = fields.Selection([
        ('inbound', 'Inbound Payment'),
        ('outbound', 'Outbound Payment'),
    ], default='inbound', string='Payment Type', required=True)
    total_amount = fields.Float(string='Total Amount')
    payment_date = fields.Datetime(string='Payment Date')
    arise_date = fields.Datetime(string='Arise Date')
    booking_id = fields.Many2one('mapstar.booking', string='Mapstar Booking')
    property_id = fields.Many2one('mapstar.property', string='Mapstar Property')
    is_net = fields.Boolean(string='Is Net', default=False)
    
