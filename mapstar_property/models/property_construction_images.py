from odoo import models, fields, api


class PropertyConstructionImages(models.Model):
    _name = 'property.construction.images'
    _description = 'Property Construction Images'
    _order = 'id desc'

    construction_id = fields.Many2one('mapstar.property.construction', required=True, string='Mapstar Property Construction')
    name = fields.Char(string='Construction Image Name', required=True)
    date = fields.Date(string='Construction Image Date', required=True)
    title = fields.Char(string='Construction Image Title', compute='compute_title', store=True)

    @api.depends('name', 'date')
    def compute_title(self):
        for rec in self:
            rec.title = f'{rec.date} - {rec.name}'