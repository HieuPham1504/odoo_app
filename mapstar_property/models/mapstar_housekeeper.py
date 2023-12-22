from odoo import models, fields, api


class MapstarHouseKeeper(models.Model):
    _name = 'mapstar.housekeeper'
    _description = 'Mapstar HouseKeeper'
    _order = 'id desc'

    code = fields.Char(string='HouseKeeper Code')
    name = fields.Char(string='HouseKeeper Name', required=True)
    phone = fields.Char(string='HouseKeeper Phone', required=True)
    type = fields.Selection([
        ('housekeeper', 'HouseKeeper'),
        ('service_manager', 'Manager'),
    ], string='HouseKeeper Type')
