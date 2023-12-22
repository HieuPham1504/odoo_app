from odoo import models, fields, api


class MapstarContract(models.Model):
    _name = 'mapstar.contract'
    _description = 'Mapstar Contract'
    _order = 'id desc'

    property_id = fields.Many2one('mapstar.property', string='Mapstar Property')
    name = fields.Char(string='Contract Name', required=True)
    contract_file = fields.Binary(string='Contract File')
    state = fields.Selection([
        ('unsign', 'UnSign Contract'),
        ('signed', 'Signed Contract'),
        ('expired', 'Expired Contract'),
    ], default='unsign')