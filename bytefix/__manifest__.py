
{
    'name': 'ByteFix - Gestión de Reparaciones',
    'version': '19.0.1.0.0',
    'summary': 'Gestión de clientes, equipos y reparaciones informáticas',
    'description': """  'Aplicación para gestionar un taller de reparación informática.
                        Permite organizar clientes, equipos y reparaciones.' """,
    'category': 'Services',
    'author': 'David Cordon Garrido',
    'depends': ['base'],
    'data': [
    'security/ir.model.access.csv',
    'views/cliente_views.xml',
    'views/equipo_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
