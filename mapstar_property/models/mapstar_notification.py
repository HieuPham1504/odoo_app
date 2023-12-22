from odoo import models, fields, api

class MapstarNotification(models.Model):
    _name = 'mapstar.notification'
    _description = 'Mapstar Notification'
    _order = 'id desc'

    name = fields.Char(string='Notification Name', required=True)
    notification_type = fields.Selection([
        ('all', 'All user'),
        ('group', 'Group User'),
        ('manual', 'Manual Notification'),
    ], string='Notification Type')
    send_method = fields.Selection([
        ('now', 'Send Now'),
        ('schedule', 'Schedule'),
    ], default='now', string='Send Method', required=True)
    icon = fields.Selection([
        ('warning', 'Warning Notification'),
        ('star', 'Star Notification'),
        ('info', 'Info Notification'),
    ], default='info', string='Notification Icon', required=True)
    link = fields.Text(string='Notification Link')
    title = fields.Char(string='Notification Title', required=True)
    content = fields.Text(string='Notification Content', required=True)
    user_ids = fields.Many2many('res.users', 'notification_users_rel', 'notification_id', 'user_id', string='Notification Users')
    group_ids = fields.Many2many('res.groups', 'notification_group_rel', 'notification_id', 'group_id', string='Notification Groups')
    state = fields.Selection([
        ('draft', 'Draft Notification'),
        ('sent', 'Sent Notification'),
        ('seen', 'Seen Notification'),
    ], default='draft', string='Notification State', required=True)
    date_schedule = fields.Datetime(string='Date Schedule')
