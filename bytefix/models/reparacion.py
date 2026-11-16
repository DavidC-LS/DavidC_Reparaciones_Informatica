from odoo import models, fields, api
from odoo.exceptions import ValidationError

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
    dias_estimados = fields.Integer(string="Días estimados de reparación",
                        compute="_compute_dias_estimados")


    #Comprobacion de que el coste estimado no sea negativo, se usa api.constraints
    #para que se ejecute cada vez que se modifique el campo coste_estimado,
    #y si es negativo se lanza un error de validacion.
    @api.constraints("coste_estimado")
    def validar_coste_estimado(self):
        for reparacion in self:
            if reparacion.coste_estimado < 0:
                raise ValidationError("El coste estimado no puede ser negativo.")


    #Calcula cuantos dias hay entre la entrada del equipo y la fecha prevista de entrega,
    #si falta alguna fecha pone 0, si la fecha prevista es anterior a la fecha de entrada lanza un error,
    #se usa api.depends para que se ejecute cada vez que se modifique alguno de los dos campos
    @api.depends("fecha_entrada", "fecha_prevista")
    def _compute_dias_estimados(self):
        for reparacion in self:
            if not reparacion.fecha_entrada or not reparacion.fecha_prevista:
                reparacion.dias_estimados = 0
                continue

            dias = (reparacion.fecha_prevista - reparacion.fecha_entrada.date()).days

            if dias < 0:
                raise ValidationError("La fecha prevista no puede ser anterior a la fecha de entrada.")

            reparacion.dias_estimados = dias