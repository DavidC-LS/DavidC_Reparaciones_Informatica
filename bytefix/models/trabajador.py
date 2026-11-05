from odoo import models, fields 

class Trabajador(models.Model):
    _name = 'bytefix.trabajador'
    _description = 'Trabajador de ByteFix'

    nombre = fields.Char(string="Nombre")
    apellido = fields.Char(string = "Apellido")
    email = fields.Char(string="Email")
    dni = fields.Char(string="DNI")
    telefono = fields.Char(string="Telefono")
    fecha_contratacion = fields.Date(string="Fecha de contratacion")
    activo = fields.Boolean(string="Activo")
    foto = fields.Binary(string="Foto del trabajador")
    especialidad = fields.Selection( [
            ('hardware', 'Hardware'),
            ('software', 'Software'),
        ],
        string="Especialidad del trabajador"
        )
    salario = fields.Float(string="Salario")
    observaciones = fields.Text(string="Observaciones")
    reparacion_ids = fields.Many2many(
        'bytefix.reparacion',
        string = "Reparaciones asignadas"
    )