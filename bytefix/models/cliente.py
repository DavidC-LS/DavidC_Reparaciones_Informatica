from odoo import models, fields

class Cliente(models.Model):
    _name = 'bytefix.cliente'
    _description = 'Cliente de ByteFix'

    nombre = fields.Char(string="Nombre")
    apellidos = fields.Char(string="Apellidos")
    email = fields.Char(string="Email")
    direccion = fields.Char(string="Direccion")
    telefono = fields.Char(string="Teléfono")
    fecha_alta = fields.Date(string="Fecha de alta")
    habitual = fields.Boolean(string="Cliente habitual")
    foto = fields.Binary(string="Foto del cliente")
    notas = fields.Text(string="Observaciones")
    