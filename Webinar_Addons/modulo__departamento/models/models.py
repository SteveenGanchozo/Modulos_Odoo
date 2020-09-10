# -*- coding: utf-8 -*-

from odoo import models, fields


class Departamento(models.Model):
  _name = "reg.departamento"
  _description = "Servidor Publico de la UNL"

  name = fields.Char(string="Nombre")

