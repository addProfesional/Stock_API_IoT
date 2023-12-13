from flask import Blueprint, request, jsonify
from ..models.InventoryModel import InventoryModel
from ..database.Database import db
from ..utils.SecurityUtils import Security

router = Blueprint('inventory_blueprint', __name__)

@router.before_request
def verificar_token():
    tiene_acceso = Security.verificar_token(request.headers)
    if not tiene_acceso: return jsonify({'error': 'No está autorizado para realizar la petición'}), 401

@router.route('/',  methods=['GET'])
def obtenerInventarios():
    # Obtener usuarios desde la base de datos utilizando el modelo
    inventarios = InventoryModel.query.all()

    # Convertir a un formato JSON o cualquier otro formato necesario
    resultado = [{'id': inventario.inventory_id, 'name': inventario.name} for inventario in inventarios]

    return jsonify(resultado), 200

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
    # Validar que el campo sea uno de los campos válidos del modelo Usuario
    campos_validos = [columna.name for columna in InventoryModel.__table__.columns]
    if field not in campos_validos:
        return jsonify({'error': 'Campo no válido'}), 400

    # Construir la consulta dinámica
    filtro = {field: value}
    print(filtro)
    inventario = InventoryModel.query.filter_by(**filtro).first()
    print(inventario)

    if inventario:
        resultado = {
            'id': inventario.inventory_id,
            'name': inventario.name,
            'quantity': inventario.quantity
        }
        return jsonify(resultado), 200
    else:
        return jsonify({'error': 'Inventario no encontrado'}), 404

@router.route('/actualizarInventario/<string:field>/<string:value>',  methods=['POST'])
def actualizarInventario(field, value):
    datos_json = request.json
    # Validar que el campo sea uno de los campos válidos del modelo Usuario
    campos_validos = [columna.name for columna in InventoryModel.__table__.columns]
    if field not in campos_validos:
        return jsonify({'error': 'Campo no válido'}), 400

    # Construir la consulta dinámica
    filtro = {field: value}
    print(filtro)
    inventario = InventoryModel.query.filter_by(**filtro).first()
    print(inventario)

    inventario.name = datos_json['name']
    inventario.quantity = datos_json['quantity']

    db.session.commit()

    return jsonify({'msg': 'Inventario ' +str(inventario.inventory_id)+ ' actualizado' }), 200

@router.route('/eliminarInventario/<string:field>/<string:value>',  methods=['DELETE'])
def eliminarInventario(field, value):
    # Validar que el campo sea uno de los campos válidos del modelo Usuario
    campos_validos = [columna.name for columna in InventoryModel.__table__.columns]
    if field not in campos_validos:
        return jsonify({'error': 'Campo no válido'}), 400

    # Construir la consulta dinámica
    filtro = {field: value}
    print(filtro)
    inventario = InventoryModel.query.filter_by(**filtro).first()
    print(inventario)

    db.session.delete(inventario)
    db.session.commit()

    return jsonify({'msg': 'Usuario ' +str(inventario.inventory_id)+ ' eliminado'}), 200