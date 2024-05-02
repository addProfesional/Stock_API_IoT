from flask import Blueprint, request, jsonify
from ..models.HistoryModel import HistoryModel
from ..models.CardsModel import CardsModel
from ..models.DevicesModel import DevicesModel
from ..database.Database import db
from ..utils.SecurityUtils import Security

import time

router = Blueprint('history_blueprint', __name__)

@router.before_request
def verificar_token():
    tiene_acceso = Security.verificar_token(request.headers)
    if not tiene_acceso: return jsonify({'error': 'No está autorizado para realizar la petición'}), 401

@router.route('/',  methods=['GET'])
def obtenerHistoriales():
    # Obtener usuarios desde la base de datos utilizando el modelo
    historias = HistoryModel.query.all()

    # Convertir a un formato JSON o cualquier otro formato necesario
    resultado = [{'id': historia.history_id, 'type': historia.type} for historia in historias]

    return jsonify(resultado), 200

@router.route('/crear',  methods=['POST'])
def crearHistorial():
    datos_json = request.json

    # Crear una instancia del modelo a partir de los datos JSON
    nueva_historia = HistoryModel.crear_desde_json(datos_json)
    print(nueva_historia)

    # Agregar la nueva instancia a la base de datos y hacer commit
    db.session.add(nueva_historia)
    db.session.commit()

    return jsonify({'msg': {'id': nueva_historia.history_id, 'type': nueva_historia.type}})

@router.route('/transaccionar/stock',  methods=['POST'])
def transaccionarStock():
    print('Entra a transaccionarStock(): ')
    datos_json = request.json
    print(datos_json)

    #Consultar datos del card:
    queryCard = {'uuid_card': datos_json['id']}
    card = CardsModel.query.filter_by(**queryCard).first()
    print(card)

    userId = card.user_id
    print(userId)

    #Consultar datos del dispositivo
    queryDevice = {'name': datos_json['device_name']}
    device = DevicesModel.query.filter_by(**queryDevice).first()

    deviceId = device.device_id

    dataToWrite = {
        'type' : 'AccessIn',
        'user_id' : userId,
        'device_id' : deviceId,
        'inventory_id': None,
        'merchant_id' : None,
        'created_at': int(time.time() * 1000),
        'deleted' : False
    }

    # Crear una instancia del modelo a partir de los datos JSON
    nueva_historia = HistoryModel.crear_desde_json(dataToWrite)
    print(nueva_historia)

    # Agregar la nueva instancia a la base de datos y hacer commit
    db.session.add(nueva_historia)
    db.session.commit()

    return jsonify({'msg': {'id': nueva_historia.history_id, 'type': nueva_historia.type, 'status': True}})

@router.route('/obtenerHistoria/<string:field>/<string:value>',  methods=['GET'])
def obtenerHistorial(field, value):
    # Validar que el campo sea uno de los campos válidos del modelo Usuario
    campos_validos = [columna.name for columna in HistoryModel.__table__.columns]
    if field not in campos_validos:
        return jsonify({'error': 'Campo no válido'}), 400

    # Construir la consulta dinámica
    filtro = {field: value}
    print(filtro)
    historia = HistoryModel.query.filter_by(**filtro).first()
    print(historia)

    if historia:
        resultado = {
            'id': historia.history_id,
            'type': historia.type
        }
        return jsonify(resultado), 200
    else:
        return jsonify({'error': 'Historia no encontrada'}), 404

@router.route('/actualizarHistoria/<string:field>/<string:value>',  methods=['POST'])
def actualizarHistorial(field, value):
    datos_json = request.json
    # Validar que el campo sea uno de los campos válidos del modelo Usuario
    campos_validos = [columna.name for columna in HistoryModel.__table__.columns]
    if field not in campos_validos:
        return jsonify({'error': 'Campo no válido'}), 400

    # Construir la consulta dinámica
    filtro = {field: value}
    print(filtro)
    historia = HistoryModel.query.filter_by(**filtro).first()
    print(historia)

    historia.type = datos_json['type']
    # Agregar los campos correspondientes

    return jsonify({'msg': 'Historia ' +str(historia.history_id)+ ' actualizada' }), 200

@router.route('/eliminarHistoria/<string:field>/<string:value>',  methods=['DELETE'])
def eliminarHistorial(field, value):
    # Validar que el campo sea uno de los campos válidos del modelo Usuario
    campos_validos = [columna.name for columna in HistoryModel.__table__.columns]
    if field not in campos_validos:
        return jsonify({'error': 'Campo no válido'}), 400

    # Construir la consulta dinámica
    filtro = {field: value}
    print(filtro)
    historia = HistoryModel.query.filter_by(**filtro).first()
    print(historia)

    db.session.delete(historia)
    db.session.commit()

    return jsonify({'msg': 'Historia ' +str(historia.history_id)+ ' eliminado'}), 200