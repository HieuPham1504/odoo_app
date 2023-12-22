from odoo import models, fields, api

class PropertyConstructionPayment(models.Model):
    _name = 'property.construction.payment'
    _description = 'Property Construction Payment'
    _order = 'id desc'

    name = fields.Char(string='Construction Payment Name', required=True)
    total_amount = fields.Float(string='Construction Total Amount')
    description = fields.Char(string='Construction Payment Description')
    payment_date = fields.Date(string='Construction Payment Date', required=True)
    state = fields.Selection([
        ('partial', 'Partial Construction Payment'),
        ('paid', 'Paid Construction Payment'),
    ], string='Construction Payment State')
    property_construction_id = fields.Many2one('mapstar.property.construction', required=True)