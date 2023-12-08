from flask import Blueprint, request, jsonify

router = Blueprint('devices_blueprint', __name__)

@router.route('/',  methods=['GET'])
def obtenerDispositivos():
    return jsonify({'msg': 'Obteniendo dispositivos'})

@router.route('/crear',  methods=['POST'])
def crearDispositivo():
    return jsonify({'msg': 'Creando dispositivo'})

@router.route('/obtenerDispositivo/<string:field>/<string:value>',  methods=['GET'])
def obtenerDispositivo(field, value):
    return jsonify({'msg': 'Obteniendo un dispositivo'})

@router.route('/actualizarDispositivo/<string:field>/<string:value>',  methods=['POST'])
def actualizarDispositivo(field, value):
    return jsonify({'msg': 'Actualizando un dispositivo'})

@router.route('/eliminarDispositivo/<string:field>/<string:value>',  methods=['DELETE'])
def eliminarDispositivo(field, value):
    return jsonify({'msg': 'Eliminando un dispositivo'})