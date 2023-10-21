from flask import Blueprint, request, jsonify

router = Blueprint('devices_blueprint', __name__)

@router.route('/')
def obtenerDispositivos():
    return jsonify({'msg': 'Obteniendo dispositivos'})
