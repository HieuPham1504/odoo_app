# -*- coding: utf-8 -*-
# from odoo import http


# class MapstarProperty(http.Controller):
#     @http.route('/mapstar_property/mapstar_property', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mapstar_property/mapstar_property/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('mapstar_property.listing', {
#             'root': '/mapstar_property/mapstar_property',
#             'objects': http.request.env['mapstar_property.mapstar_property'].search([]),
#         })

#     @http.route('/mapstar_property/mapstar_property/objects/<model("mapstar_property.mapstar_property"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mapstar_property.object', {
#             'object': obj
#         })

