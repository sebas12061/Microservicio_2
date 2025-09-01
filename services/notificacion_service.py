from repositories import notificacion_repository as repo

def enviar_notificacion(data):
    mensaje = data.get("mensaje")
    tipo = data.get("tipo", "general")

    # Validación simple
    if not mensaje or mensaje.strip() == "":
        return None

    return repo.guardar_notificacion(mensaje, tipo).to_dict()

def obtener_notificaciones():
    return repo.listar_notificaciones()
