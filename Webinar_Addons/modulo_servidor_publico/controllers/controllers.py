# -*- coding: utf-8 -*-
# from odoo import http


# class ModuloServidorPublico(http.Controller):
#     @http.route('/modulo_servidor_publico/modulo_servidor_publico/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo_servidor_publico/modulo_servidor_publico/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_servidor_publico.listing', {
#             'root': '/modulo_servidor_publico/modulo_servidor_publico',
#             'objects': http.request.env['modulo_servidor_publico.modulo_servidor_publico'].search([]),
#         })

#     @http.route('/modulo_servidor_publico/modulo_servidor_publico/objects/<model("modulo_servidor_publico.modulo_servidor_publico"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_servidor_publico.object', {
#             'object': obj
#         })
