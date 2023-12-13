from flask import Blueprint, request, jsonify
from ..models.MerchantModel import MerchantModel
from ..database.Database import db
from ..utils.SecurityUtils import Security

router = Blueprint('mercancias_blueprint', __name__)

@router.before_request
def verificar_token():
    tiene_acceso = Security.verificar_token(request.headers)
    if not tiene_acceso: return jsonify({'error': 'No está autorizado para realizar la petición'}), 401

@router.route('/', methods=['GET'])
def obtenerMercancias():
    # Obtener usuarios desde la base de datos utilizando el modelo
    mercancias = MerchantModel.query.all()

    # Convertir a un formato JSON o cualquier otro formato necesario
    resultado = [{'id': mercancia.merchant_id, 'nombre': mercancia.name, 'deleted': mercancia.deleted} for mercancia in mercancias]

    return jsonify(resultado), 200

@router.route('/crear',  methods=['POST'])
def crearMercancia():
    datos_json = request.json

    # Crear una instancia del modelo a partir de los datos JSON
    nueva_mercancia = MerchantModel.crear_desde_json(datos_json)

    # Agregar la nueva instancia a la base de datos y hacer commit
    db.session.add(nueva_mercancia)
    db.session.commit()

    return jsonify({'msg': {'id': nueva_mercancia.merchant_id, 'nombre': nueva_mercancia.name}})

@router.route('/obtenerMercancia/<string:field>/<string:value>',  methods=['GET'])
def obtenerMercancia(field, value):
    # Validar que el campo sea uno de los campos válidos del modelo Usuario
    campos_validos = [columna.name for columna in MerchantModel.__table__.columns]
    if field not in campos_validos:
        return jsonify({'error': 'Campo no válido'}), 400

    # Construir la consulta dinámica
    filtro = {field: value}
    print(filtro)
    mercancia = MerchantModel.query.filter_by(**filtro).first()
    print(mercancia)

    if mercancia:
        resultado = {
            'id': mercancia.merchant_id,
            'name': mercancia.name,
            'unit_of_measure': mercancia.unit_of_measure
        }
        return jsonify(resultado), 200
    else:
        return jsonify({'error': 'Mercancia no encontrada'}), 404

@router.route('/actualizarMercancia/<string:field>/<string:value>',  methods=['POST'])
def actualizarMercancia(field, value):
    datos_json = request.json
    campos_validos = [columna.name for columna in MerchantModel.__table__.columns]
    if field not in campos_validos:
        return jsonify({'error': 'Campo no válido'}), 400

    # Construir la consulta dinámica
    filtro = {field: value}
    print(filtro)
    mercancia = MerchantModel.query.filter_by(**filtro).first()
    print(mercancia)

    mercancia.categories = datos_json['categories']
    mercancia.name = datos_json['name']
    # Agregar mas campos

    db.session.commit()

    return jsonify({'msg': 'Mercancia ' +str(mercancia.merchant_id)+ ' actualizada' }), 200

@router.route('/eliminarMercancia/<string:field>/<string:value>',  methods=['DELETE'])
def eliminarMercancia(field, value):
    campos_validos = [columna.name for columna in MerchantModel.__table__.columns]
    if field not in campos_validos:
        return jsonify({'error': 'Campo no válido'}), 400

    # Construir la consulta dinámica
    filtro = {field: value}
    print(filtro)
    mercancia = MerchantModel.query.filter_by(**filtro).first()
    print(mercancia)

    db.session.delete(mercancia)
    db.session.commit()

    return jsonify({'msg': 'Mercancia ' +str(mercancia.merchant_id)+ ' eliminada'}), 200