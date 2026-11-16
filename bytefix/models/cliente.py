from odoo import models, fields, api

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
    reparacion_ids = fields.One2many(
    'bytefix.reparacion',
    'cliente_id',
    string="Reparaciones"
)
    total_reparaciones = fields.Integer(
    string="Total de reparaciones",
    compute="_compute_total_reparaciones",
)

    #Cuenta cuantas reparaciones tiene el cliente, se usa api.depends para que se ejecute cada vez que se modifique el campo reparacion_ids
    @api.depends("reparacion_ids")
    def _compute_total_reparaciones(self):
        for cliente in self:
            cliente.total_reparaciones = len(cliente.reparacion_ids)