# -*- coding: utf-8 -*-
from odoo import http

# class ObraCivil2(http.Controller):
#     @http.route('/obra_civil_2/obra_civil_2/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/obra_civil_2/obra_civil_2/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('obra_civil_2.listing', {
#             'root': '/obra_civil_2/obra_civil_2',
#             'objects': http.request.env['obra_civil_2.obra_civil_2'].search([]),
#         })

#     @http.route('/obra_civil_2/obra_civil_2/objects/<model("obra_civil_2.obra_civil_2"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('obra_civil_2.object', {
#             'object': obj
#         })