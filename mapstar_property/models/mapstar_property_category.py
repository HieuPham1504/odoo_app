from odoo import models, fields, api


class MapstarPropertyCategory(models.Model):
    _name = 'mapstar.property.category'
    _description = 'Mapstar Property Category'
    _order = 'id desc'

    name = fields.Char(string='Category Name', required=True)
    description = fields.Text(string='Category Description')