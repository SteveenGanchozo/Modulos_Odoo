# -*- coding: utf-8 -*-
# from odoo import http


# class ModuloDepartamento(http.Controller):
#     @http.route('/modulo__departamento/modulo__departamento/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo__departamento/modulo__departamento/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo__departamento.listing', {
#             'root': '/modulo__departamento/modulo__departamento',
#             'objects': http.request.env['modulo__departamento.modulo__departamento'].search([]),
#         })

#     @http.route('/modulo__departamento/modulo__departamento/objects/<model("modulo__departamento.modulo__departamento"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo__departamento.object', {
#             'object': obj
#         })
