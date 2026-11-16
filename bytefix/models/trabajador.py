from odoo import models, fields, api
from odoo.exceptions import ValidationError

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
    reparaciones_pendientes = fields.Integer( string = "Reparaciones pendientes",
        compute = "_compute_reparaciones_pendientes"
        )
    @api.depends("reparacion_ids", "reparacion_ids.estado")
    def _compute_reparaciones_pendientes(self):
        for trabajador in self:
            reparaciones_pendientes = 0
            for reparacion in trabajador.reparacion_ids:
                if reparacion.estado in ('recibido', 'en reparacion'):
                    reparaciones_pendientes += 1
            trabajador.reparaciones_pendientes = reparaciones_pendientes

    @api.constraints("fecha_contratacion")
    def _validar_fecha_contratacion(self):
        for trabajador in self:
            hoy = fields.Date.context_today(trabajador)
            if trabajador.fecha_contratacion and trabajador.fecha_contratacion > hoy:
                raise ValidationError("La fecha de contratación no puede ser futura.")

    @api.constraints("salario")
    def _validar_salario(self):
        for trabajador in self:
            if trabajador.salario < 0:
                raise ValidationError("El salario no puede ser negativo.")