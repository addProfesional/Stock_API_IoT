from flask import Blueprint, request, jsonify

router = Blueprint('mercancias_blueprint', __name__)

@router.route('/', methods=['GET'])
def obtenerMercancias():
    return jsonify({ 'msg': 'Obteniendo las mercancías'})

@router.route('/crear',  methods=['POST'])
def crearMercancia():
    return jsonify({'msg': 'Creando mercancía'})

@router.route('/obtenerMercancia/<string:field>/<string:value>',  methods=['GET'])
def obtenerMercancia(field, value):
    return jsonify({'msg': 'Obteniendo una mercancia'})

@router.route('/actualizarMercancia/<string:field>/<string:value>',  methods=['POST'])
def actualizarMercancia(field, value):
    return jsonify({'msg': 'Actualizando una mercancia'})

@router.route('/eliminarMercancia/<string:field>/<string:value>',  methods=['DELETE'])
def eliminarMercancia(field, value):
    return jsonify({'msg': 'Eliminando una mercancia'})