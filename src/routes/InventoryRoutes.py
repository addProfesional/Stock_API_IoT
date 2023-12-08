from flask import Blueprint, request, jsonify

router = Blueprint('inventory_blueprint', __name__)

@router.route('/',  methods=['GET'])
def obtenerInventarios():
    return jsonify({'msg': 'Obteniendo inventarios'})

@router.route('/crear',  methods=['POST'])
def crearInventario():
    return jsonify({'msg': 'Creando inventario'})

@router.route('/obtenerInventario/<string:field>/<string:value>',  methods=['GET'])
def obtenerInventario(field, value):
    return jsonify({'msg': 'Obteniendo un inventario'})

@router.route('/actualizarInventario/<string:field>/<string:value>',  methods=['POST'])
def actualizarInventario(field, value):
    return jsonify({'msg': 'Actualizando un inventario'})

@router.route('/eliminarInventario/<string:field>/<string:value>',  methods=['DELETE'])
def eliminarInventario(field, value):
    return jsonify({'msg': 'Eliminando un inventario'})