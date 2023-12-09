from flask import Blueprint, request, jsonify
from ..models.InventoryModel import InventoryModel
from ..database.Database import db

router = Blueprint('inventory_blueprint', __name__)

@router.route('/',  methods=['GET'])
def obtenerInventarios():
    return jsonify({'msg': 'Obteniendo inventarios'})

@router.route('/crear',  methods=['POST'])
def crearInventario():
    datos_json = request.json

    # Crear una instancia del modelo a partir de los datos JSON
    nuevo_inventario = InventoryModel.crear_desde_json(datos_json)

    # Agregar la nueva instancia a la base de datos y hacer commit
    db.session.add(nuevo_inventario)
    db.session.commit()

    return jsonify({'msg': {'id': nuevo_inventario.inventory_id, 'nombre': nuevo_inventario.name}})

@router.route('/obtenerInventario/<string:field>/<string:value>',  methods=['GET'])
def obtenerInventario(field, value):
    return jsonify({'msg': 'Obteniendo un inventario'})

@router.route('/actualizarInventario/<string:field>/<string:value>',  methods=['POST'])
def actualizarInventario(field, value):
    return jsonify({'msg': 'Actualizando un inventario'})

@router.route('/eliminarInventario/<string:field>/<string:value>',  methods=['DELETE'])
def eliminarInventario(field, value):
    return jsonify({'msg': 'Eliminando un inventario'})