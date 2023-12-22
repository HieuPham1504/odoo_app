from odoo import models, fields, api


class MapstarPropertyConstruction(models.Model):
    _name = 'mapstar.property.construction'
    _description = 'Mapstar Property Construction'
    _order = 'id desc'

    name = fields.Char(string='Construction Name', required=True)
    property_id = fields.Many2one('mapstar.property', string='Mapstar Property', required=True)
    owner_id = fields.Many2one('res.partner', string='Property Owner', related='property_id.owner_id')
    address = fields.Char(string='Property Address', related='property_id.street')
    start_date = fields.Date(string='Start Date')
    date_schedule = fields.Date(string='Date Schedule')
    done_date = fields.Date(string='Done Date')
    description = fields.Text(string='Construction Description')
    construction_line_ids = fields.One2many('mapstar.property.construction.line', 'construction_id', string='Construction Lines')
    construction_payment_ids = fields.One2many('property.construction.payment', 'property_construction_id', string='Property Construction Payment')
    construction_image_ids = fields.One2many('property.construction.images', 'construction_id', string='Property Construction Images')
    state = fields.Selection([
        ('draft', 'Draft Construction'),
        ('constructing', 'Constructing Construction'),
        ('complete', 'Complete Construction'),
    ], default='draft', string='Construction State')

class MapstarPropertyConstructionLine(models.Model):
    _name = 'mapstar.property.construction.line'
    _description = 'Mapstar Property Construction Line'
    _order = 'id desc'

    construction_id = fields.Many2one('mapstar.property.construction', required=True, string='Mapstar Property Construction')
    name = fields.Char(string='Construction Line Name', required=True)
    rate = fields.Char(string='Construction Line Rate', required=True)
    done_date = fields.Date(string='Construction Line Done Date')
    state = fields.Selection([
        ('prepare', 'Prepare Construction'),
        ('constructing', 'Constructing Construction'),
        ('complete', 'Complete Construction'),
    ], default='prepare', string='Construction State')