# -*- coding: utf-8 -*-
# from odoo import http


# class MServidorPublico(http.Controller):
#     @http.route('/m_servidor_publico/m_servidor_publico/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/m_servidor_publico/m_servidor_publico/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('m_servidor_publico.listing', {
#             'root': '/m_servidor_publico/m_servidor_publico',
#             'objects': http.request.env['m_servidor_publico.m_servidor_publico'].search([]),
#         })

#     @http.route('/m_servidor_publico/m_servidor_publico/objects/<model("m_servidor_publico.m_servidor_publico"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('m_servidor_publico.object', {
#             'object': obj
#         })
