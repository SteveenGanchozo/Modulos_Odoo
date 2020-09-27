# -*- coding: utf-8 -*-
# from odoo import http


# class MDepartamento(http.Controller):
#     @http.route('/m_departamento/m_departamento/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/m_departamento/m_departamento/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('m_departamento.listing', {
#             'root': '/m_departamento/m_departamento',
#             'objects': http.request.env['m_departamento.m_departamento'].search([]),
#         })

#     @http.route('/m_departamento/m_departamento/objects/<model("m_departamento.m_departamento"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('m_departamento.object', {
#             'object': obj
#         })
