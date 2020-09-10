# -*- coding: utf-8 -*-

from odoo import models, fields


class Servidor(models.Model):
  _name = "reg.servidor"
  _description = "Servidor Publico de la UNL"

  #servidor_P = fields.Many2one('reg.servidor_p', 'Servidor_P:')
  name = fields.Char(string="Nombre")
