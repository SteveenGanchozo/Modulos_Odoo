# -*- coding: utf-8 -*-
# from odoo import http


# class MEncuesta(http.Controller):
#     @http.route('/m_encuesta/m_encuesta/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/m_encuesta/m_encuesta/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('m_encuesta.listing', {
#             'root': '/m_encuesta/m_encuesta',
#             'objects': http.request.env['m_encuesta.m_encuesta'].search([]),
#         })

#     @http.route('/m_encuesta/m_encuesta/objects/<model("m_encuesta.m_encuesta"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('m_encuesta.object', {
#             'object': obj
#         })
