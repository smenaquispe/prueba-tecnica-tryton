from trytond.module import register

register(
    'my_module',  # Nombre del módulo
    1, 0,  # Versión
    depends=['ir'],  # Dependencias (puedes agregar más si es necesario)
    label='My Module',  # Nombre amigable
)

