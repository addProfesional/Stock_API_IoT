from flask import Blueprint, request, jsonify

router = Blueprint('history_blueprint', __name__)

@router.route('/',  methods=['GET'])
def obtenerHistoriales():
    return jsonify({'msg': 'Obteniendo Historiales'})

@router.route('/crear',  methods=['POST'])
def crearHistorial():
    return jsonify({'msg': 'Creando historia'})

@router.route('/obtenerHistoria/<string:field>/<string:value>',  methods=['GET'])
def obtenerHistorial(field, value):
    return jsonify({'msg': 'Obteniendo un historia'})

@router.route('/actualizarHistoria/<string:field>/<string:value>',  methods=['POST'])
def actualizarHistorial(field, value):
    return jsonify({'msg': 'Actualizando un historia'})

@router.route('/eliminarHistoria/<string:field>/<string:value>',  methods=['DELETE'])
def eliminarHistorial(field, value):
    return jsonify({'msg': 'Eliminando un historia'})