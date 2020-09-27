# -*- coding: utf-8 -*-

from odoo import models, fields


class encuesta(models.Model):
     _name = 'reg.encuesta'
     _description = 'Datos Encuesta'

     name = fields.Char(string="Título")
     fecha = fields.Datetime('Fecha', required=False, readonly=False, select=True
                                , default=lambda self: fields.datetime.now())

class encuesta_satisfaccion(encuesta):
     _name = 'reg.encuesta_satisfaccion'
     _description = 'Datos Encuesta satisfaccion'

     
class encuesta_actividades(encuesta):
     _name = 'reg.encuesta_actividades'
     _description = 'Datos encuesta actividades'

