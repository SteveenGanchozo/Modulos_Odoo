# -*- coding: utf-8 -*-

from odoo import models, fields


class Encuesta(models.Model):
  _name = "reg.encuesta"
  _description = "Encuesta"

  #servidor_P = fields.Many2one('reg.servidor_p', 'Servidor_P:')
  nombrer = fields.Char(string="Nombre")

