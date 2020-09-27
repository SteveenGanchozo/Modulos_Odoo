# -*- coding: utf-8 -*-

from odoo import models, fields

class Persona(models.Model):
     _name = 'reg.Persona'
     _description = 'Datos Persona'

     name = fields.Char(string="Nombres")
     apellidos = fields.Char(string="Apellidos")
     cedula = fields.Char(string="Cédula")
     correo = fields.Char(string="Correo")

class servidor_publico(Persona):
     _name = 'reg.servidor_publicos'
     _description = 'Datos Servidor Público'

     departamento= fields.Many2one('m_departamento.m_departamento', ondelete='cascade', string="Departamento", required=True)
     cargo = fields.Char(string="Cargo")
     
class encargado_migracion(Persona):
     _name = 'reg.encargado_migracion'
     _description = 'Datos Encargado Migraciónes'
     
     usuario = fields.Char(string="Usuario")
     contraseña = fields.Char(string="Contraseña")

#class m_encuesta(models.Model):
#     _name = 'm_encuesta.m_encuesta'
#     _description = 'Encuestas'

#     name = fields.Char(string="Título")
#     fecha = fields.Char(string="Fecha")

#class encuesta_satisfaccion(m_encuesta):
#     _name = 'reg.encuesta_satisfaccion'
#     _description = 'Datos encuesta_satisfaccion'
     
#class encuesta_actividad(m_encuesta):
#     _name = 'reg.encuesta_actividad'
#     _description = 'Datos encuesta_actividad'
