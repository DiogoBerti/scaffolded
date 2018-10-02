# -*- coding: utf-8 -*-
from odoo import http

# class Scaffolded(http.Controller):
#     @http.route('/scaffolded/scaffolded/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/scaffolded/scaffolded/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('scaffolded.listing', {
#             'root': '/scaffolded/scaffolded',
#             'objects': http.request.env['scaffolded.scaffolded'].search([]),
#         })

#     @http.route('/scaffolded/scaffolded/objects/<model("scaffolded.scaffolded"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('scaffolded.object', {
#             'object': obj
#         })