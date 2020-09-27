# -*- coding: utf-8 -*-

from odoo import models, fields

class m_departamento(models.Model):
   _name = 'm_departamento.m_departamento'
   _description = 'Departamentos'

   name = fields.Char(string="Nombre del Depatmento")


