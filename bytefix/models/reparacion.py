from odoo import models, fields

class Reparacion(models.Model):
    _name = 'bytefix.reparacion'
    _description = 'Informacion de las reparaciones'
    
    numero_reparacion = fields.Char(string="Numero de reparación")
    cliente_id = fields.Many2one(
    'bytefix.cliente',
    string="Cliente"
    )
    equipo_id = fields.Many2one(
    'bytefix.equipo',
    string="Equipo"
    )

    trabajadores_ids = fields.Many2many(
    'bytefix.trabajador',
    string="Trabajadores asignados"
    )
    fecha_entrada = fields.Datetime(string="Fecha de entrada")
    estado = fields.Selection(
    [
        ('recibido', 'Recibido'),
        ('en reparacion', 'En reparación'),
        ('finalizada', 'Finalizada'),
        ('entregada','Entregada'),
    ],
    string="Estado de la reparación"
    )
    fecha_prevista = fields.Date(string="Fecha de entrega prevista")
    urgente = fields.Boolean(string="Prioridad")
    coste_estimado = fields.Float(string="Presupuesto")
    descripcion = fields.Text(string="Problemas del equipo")
        