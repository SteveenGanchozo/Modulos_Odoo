# -*- coding: utf-8 -*-

from odoo import models, fields


class Persona(models.Model):
     _name = 'reg.persona'
     _description = 'Datos Persona'

     name = fields.Char(string="Nombres")
     apellidos = fields.Char(string="Apellidos")
     cedula = fields.Char(string="Cédula")
     correo = fields.Char(string="Correo")

class Servidor_publico(Persona):
     _name = 'reg.servidor_publico'
     _description = 'Datos Servidor Público'

     departamento= fields.Many2one('m_departamento.m_departamento', ondelete='cascade', string="Departamento", required=True)
     cargo = fields.Char(string="Cargo")
     
class Encargado_migracion(Persona):
     _name = 'reg.encargado_migracion'
     _description = 'Datos Encargado Migración'
     
     usuario = fields.Char(string="Usuario")
     contraseña = fields.Char(string="Contraseña")
