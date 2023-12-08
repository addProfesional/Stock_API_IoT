from flask import Blueprint, request, jsonify
from ..models.DevicesModel import DevicesModel
from ..database.Database import db

router = Blueprint('devices_blueprint', __name__)

@router.route('/',  methods=['GET'])
def obtenerDispositivos():
    return jsonify({'msg': 'Obteniendo dispositivos'})

@router.route('/crear',  methods=['POST'])
def crearDispositivo():
    datos_json = request.json

    # Crear una instancia del modelo a partir de los datos JSON
    nuevo_dispositivo = DevicesModel.crear_desde_json(datos_json)
    print(nuevo_dispositivo)

    # Agregar la nueva instancia a la base de datos y hacer commit
    db.session.add(nuevo_dispositivo)
    db.session.commit()

    return jsonify({'msg': {'id': nuevo_dispositivo.device_id, 'nombre': nuevo_dispositivo.name}})
    # return jsonify({'msg': 'Creando dispositivo'})

@router.route('/obtenerDispositivo/<string:field>/<string:value>',  methods=['GET'])
def obtenerDispositivo(field, value):
    return jsonify({'msg': 'Obteniendo un dispositivo'})

@router.route('/actualizarDispositivo/<string:field>/<string:value>',  methods=['POST'])
def actualizarDispositivo(field, value):
    return jsonify({'msg': 'Actualizando un dispositivo'})

@router.route('/eliminarDispositivo/<string:field>/<string:value>',  methods=['DELETE'])
def eliminarDispositivo(field, value):
    return jsonify({'msg': 'Eliminando un dispositivo'})