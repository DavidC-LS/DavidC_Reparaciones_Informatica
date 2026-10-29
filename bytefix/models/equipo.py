from odoo import models, fields

class Equipo(models.Model):
    _name = 'bytefix.equipo'
    _description = 'Equipos recibidos'
    
    nombre = fields.Char(string="Nombre")
    numero_serie = fields.Char(string="Numero de serie")
    marca = fields.Char(string="Marca")
    modelo = fields.Char(string="Modelo")
    tipo = fields.Selection(
    [
        ('portatil', 'Portatil'),
        ('sobremesa', 'Sobremesa'),
        ('monitor', 'Monitor'),
    ],
    string="Tipo de equipo"
    )
    fecha_compra = fields.Date(string="Fecha de compra")
    garantia = fields.Boolean(string="Garantia")
    imagen = fields.Binary(string="Foto del equipo")
    observaciones = fields.Text(string="Observaciones")
        