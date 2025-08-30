import os
from flask import Flask, request, jsonify
from datetime import datetime, timezone
from uuid import uuid4

app = Flask(__name__)

# "Base de datos" simulada en memoria
notificaciones = []

def ahora_iso():
    return datetime.now(timezone.utc).isoformat()

# Endpoint de prueba del servicio
@app.route("/salud", methods=["GET"])
def salud():
    return {
        "estado": "ok",
        "servicio": "notificaciones",
        "total": len(notificaciones)
    }, 200

# Crear una notificación
@app.route("/notificaciones", methods=["POST"])
def crear_notificacion():
    if not request.is_json:
        return {"error": "El Content-Type debe ser application/json"}, 415

    datos = request.get_json()
    usuario_id = datos.get("usuario_id")
    mensaje = datos.get("mensaje")
    tipo = datos.get("tipo", "general")

    if not usuario_id or not mensaje:
        return {"error": "Falta 'usuario_id' o 'mensaje'"}, 400

    notif = {
        "id": str(uuid4()),
        "usuario_id": usuario_id,
        "mensaje": mensaje,
        "tipo": tipo,
        "estado": "no_leida",
        "creado_en": ahora_iso()
    }
    notificaciones.append(notif)
    return notif, 201

# Listar todas las notificaciones (modo admin / simulación)
@app.route("/notificaciones", methods=["GET"])
def listar_notificaciones():
    return jsonify(notificaciones), 200

# Obtener notificaciones de un usuario específico
@app.route("/notificaciones/usuario/<usuario_id>", methods=["GET"])
def obtener_notificaciones_usuario(usuario_id):
    del_usuario = [n for n in notificaciones if n["usuario_id"] == usuario_id]
    return jsonify(del_usuario), 200

# Marcar una notificación como leída
@app.route("/notificaciones/<notif_id>/leer", methods=["PUT"])
def marcar_como_leida(notif_id):
    for n in notificaciones:
        if n["id"] == notif_id:
            n["estado"] = "leida"
            n["leido_en"] = ahora_iso()
            return n, 200
    return {"error": "Notificación no encontrada"}, 404

if __name__ == "__main__":
    puerto = int(os.getenv("PORT", "5005"))
    app.run(host="127.0.0.1", port=puerto, debug=True)
