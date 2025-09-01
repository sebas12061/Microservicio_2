from models.notificacion import Notificacion

# Simulación de "base de datos" en memoria con estados variados
notificaciones = [
    Notificacion(1, "Bienvenido a la aplicación", "info", "enviada"),
    Notificacion(2, "Tu solicitud ha sido recibida", "alerta", "pendiente"),
    Notificacion(3, "Nueva actualización disponible", "info", "enviada"),
    Notificacion(4, "Tu cuenta ha sido verificada", "confirmacion", "enviada"),
    Notificacion(5, "Error en la conexión", "error", "fallida"),
    Notificacion(6, "Recuerda completar tu perfil", "recordatorio", "pendiente"),
    Notificacion(7, "Tu contraseña ha sido cambiada", "seguridad", "enviada"),
    Notificacion(8, "Saldo insuficiente en tu cuenta", "alerta", "fallida")
]

contador_id = 9  # El próximo ID disponible

def guardar_notificacion(mensaje, tipo="general"):
    """
    Crea una nueva notificación con estado 'pendiente' por defecto.
    """
    global contador_id
    nueva = Notificacion(contador_id, mensaje, tipo, "pendiente")
    notificaciones.append(nueva)
    contador_id += 1
    return nueva

def listar_notificaciones():
    """
    Devuelve todas las notificaciones en formato dict.
    """
    return [n.to_dict() for n in notificaciones]

def listar_por_estado(estado):
    """
    Filtra notificaciones por estado (ej: enviada, pendiente, fallida).
    """
    return [n.to_dict() for n in notificaciones if n.estado == estado]
