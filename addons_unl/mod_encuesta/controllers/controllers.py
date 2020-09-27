# -*- coding: utf-8 -*-
# from odoo import http


# class ModEncuesta(http.Controller):
#     @http.route('/mod_encuesta/mod_encuesta/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mod_encuesta/mod_encuesta/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mod_encuesta.listing', {
#             'root': '/mod_encuesta/mod_encuesta',
#             'objects': http.request.env['mod_encuesta.mod_encuesta'].search([]),
#         })

#     @http.route('/mod_encuesta/mod_encuesta/objects/<model("mod_encuesta.mod_encuesta"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mod_encuesta.object', {
#             'object': obj
#         })
