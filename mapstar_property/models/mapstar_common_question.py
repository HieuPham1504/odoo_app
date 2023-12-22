from odoo import models, fields, api

class MapstarCommonQuestion(models.Model):
    _name = 'mapstar.common.question'
    _description = 'Mapstar Common Question'
    _order = 'sequence asc'

    question = fields.Text(string='Common Question', required=True)
    answer = fields.Text(string='Common Answer', required=True)
    sequence = fields.Integer(string='Sequence', default=100, required=True)

