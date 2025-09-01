from flask import Blueprint, request, jsonify
import services.notificacion_service as service

notificacion_bp = Blueprint("notificaciones", __name__)

# Crear notificación
@notificacion_bp.route("/notificaciones", methods=["POST"])
def crear_notificacion():
    data = request.get_json()
    nueva = service.enviar_notificacion(data)
    if nueva:
        return jsonify(nueva), 201
    return jsonify({"error": "El mensaje no puede estar vacío"}), 400

# Listar notificaciones
@notificacion_bp.route("/notificaciones", methods=["GET"])
def listar_notificaciones():
    return jsonify(service.obtener_notificaciones()), 200
