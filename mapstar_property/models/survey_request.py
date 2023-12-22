from odoo import models, fields, api

class SurveyRequest(models.Model):
    _name = 'survey.request'
    _description = 'Survey Request'
    _order = 'id desc'

    property_name = fields.Char(string='Property Name', required=True)
    owner_id = fields.Many2one('res.partner', string='Owner')
    max_guest = fields.Integer(string='Max Guest')
    address = fields.Char(string='Survey Address')
    location_image_ids = fields.Many2many('ir.attachment', 'ms_survey_attachment_rel', 'survey_id', 'attach_id',
                                            string='Survey Property Pictures')
    state = fields.Selection([
        ('send', 'Send Survey'),
        ('received', 'Received Survey'),
        ('survey', 'Survey'),
        ('done', 'Done Survey'),
    ], default='send', string='Survey State')

