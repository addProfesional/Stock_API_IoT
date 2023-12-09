from flask import Blueprint, request, jsonify
from ..models.HistoryModel import HistoryModel
from ..database.Database import db

router = Blueprint('history_blueprint', __name__)

@router.route('/',  methods=['GET'])
def obtenerHistoriales():
    return jsonify({'msg': 'Obteniendo Historiales'})

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

@router.route('/obtenerHistoria/<string:field>/<string:value>',  methods=['GET'])
def obtenerHistorial(field, value):
    return jsonify({'msg': 'Obteniendo un historia'})

@router.route('/actualizarHistoria/<string:field>/<string:value>',  methods=['POST'])
def actualizarHistorial(field, value):
    return jsonify({'msg': 'Actualizando un historia'})

@router.route('/eliminarHistoria/<string:field>/<string:value>',  methods=['DELETE'])
def eliminarHistorial(field, value):
    return jsonify({'msg': 'Eliminando un historia'})