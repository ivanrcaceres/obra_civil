# -*- coding: utf-8 -*-
from odoo import http

# class ObraCivil(http.Controller):
#     @http.route('/obra_civil/obra_civil/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/obra_civil/obra_civil/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('obra_civil.listing', {
#             'root': '/obra_civil/obra_civil',
#             'objects': http.request.env['obra_civil.obra_civil'].search([]),
#         })

#     @http.route('/obra_civil/obra_civil/objects/<model("obra_civil.obra_civil"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('obra_civil.object', {
#             'object': obj
#         })