from odoo import models, fields, api


class MapstarBooking(models.Model):
    _name = 'mapstar.booking'
    _description = 'Mapstar Booking'
    _order = 'check_in desc'

    name = fields.Char(string='Name', compute='compute_name', store=True, index=True)
    check_in = fields.Date(string='Check In', required=True)
    check_out = fields.Date(string='Check Out', required=True)
    no_adult = fields.Integer(string='Number of Adult')
    no_children = fields.Integer(string='Number of Children')
    customer_name = fields.Char(required=True, string='Customer Name')
    customer_email = fields.Char(string='Customer Email')
    customer_phone = fields.Char(string='Customer Phone')
    customer_request = fields.Text(string='Customer Request')
    property_id = fields.Many2one('mapstar.property', ondelete='cascade', required=True)
    total_amount = fields.Float(string='Total Amount')
    state = fields.Selection([
        ('reserve', 'Owner Booking'),
        ('book', 'Customer Booking'),
        ('lock', 'Lock Booking'),
        ('done', 'Done Booking'),
        ('cancel', 'Cancel Booking'),
    ], default='book', string='Booking State')

    @api.depends('property_id.name', 'check_in', 'check_out')
    def compute_name(self):
        for rec in self:
            rec.name = f'{rec.property_id.name} {rec.check_in} {rec.check_out}'