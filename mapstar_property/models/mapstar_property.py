from odoo import models, fields, api


class MapstarProperty(models.Model):
    _name = 'mapstar.property'
    _description = 'Mapstar Property'
    _order = 'id desc'

    code = fields.Char(string='Property Code')
    property_avatar = fields.Binary(string='Property Avatar')
    name = fields.Char(string='Property Name', required=True)
    street = fields.Char(string='Address')
    city = fields.Char(string='City')
    category_id = fields.Many2one('mapstar.property.category', string='Property Category')
    owner_id = fields.Many2one('res.partner', string='Owner', required=True, domain=[('res_partner_type', '=', 'owner')])
    owner_phone = fields.Char(string='Owner Phone', related='owner_id.phone')
    start_date = fields.Date(string='Start Date', required=True)
    max_guest = fields.Integer(string='Max Guest')
    total_size = fields.Float(string='Total Size')
    is_sample = fields.Boolean(string='Is Sample', default=False)
    booking_free = fields.Integer(string='Night Booking Free')
    furniture = fields.Selection([
        ('basic', 'Basic'),
        ('full', 'Full'),
        ('high_class', 'High Class'),
    ], default='full', string='Furniture')
    no_bedroom = fields.Integer(string='Number of Bedroom')
    no_bathroom = fields.Integer(string='Number of Bathroom')
    special_service = fields.Text(string='Special Service')
    property_picture_ids = fields.Many2many('ir.attachment', 'ms_property_ir_attachment_rel', 'property_id', 'attachment_id',
                                            string='Pictures')
    property_contract_ids = fields.One2many('mapstar.contract', 'property_id', string='Mapstar Contract')
    housekeeper_id = fields.Many2one('mapstar.housekeeper', string='HouseKeeper', domain=[('type', '=', 'housekeeper')])
    house_service_manager_id = fields.Many2one('mapstar.housekeeper', string='House Service Manager', domain=[('type', '=', 'service_manager')])
    state = fields.Selection([
        ('draft', 'Draft Property'),
        ('constructing', 'Constructing Property'),
        ('exploited', 'Exploited Property'),
    ], default='draft')
    destination_id = fields.Many2one('mapstar.destination', string='Property Destination', required=True)
    division_id = fields.Many2one('mapstar.division', string='Property Division')
    rating_ids = fields.One2many('mapstar.rating', 'property_id', string='Property Rating')

    @api.model
    def create(self, vals):
        if vals.get('code', 'New') == 'New':
            vals['code'] = self.env['ir.sequence'].next_by_code(
                'mapstar.property')
        return super(MapstarProperty, self).create(vals)


