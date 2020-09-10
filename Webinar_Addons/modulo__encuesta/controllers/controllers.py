# -*- coding: utf-8 -*-
# from odoo import http


# class ModuloEncuesta(http.Controller):
#     @http.route('/modulo__encuesta/modulo__encuesta/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo__encuesta/modulo__encuesta/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo__encuesta.listing', {
#             'root': '/modulo__encuesta/modulo__encuesta',
#             'objects': http.request.env['modulo__encuesta.modulo__encuesta'].search([]),
#         })

#     @http.route('/modulo__encuesta/modulo__encuesta/objects/<model("modulo__encuesta.modulo__encuesta"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo__encuesta.object', {
#             'object': obj
#         })
