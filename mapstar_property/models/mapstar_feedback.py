from odoo import models, fields, api

class MapstarFeedback(models.Model):
    _name = 'mapstar.feedback'
    _description = 'Mapstar Feedback'
    _order = 'id desc'

    title = fields.Char(string='Feedback Title', required=True)
    property_id = fields.Many2one('mapstar.property', required=True, string='Mapstar Property')
    description = fields.Text(string='Feedback description')


