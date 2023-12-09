from flask import Blueprint, request, jsonify
from ..models.MerchantModel import MerchantModel
from ..database.Database import db

router = Blueprint('mercancias_blueprint', __name__)

@router.route('/', methods=['GET'])
def obtenerMercancias():
    # Obtener usuarios desde la base de datos utilizando el modelo
    mercancias = MerchantModel.query.all()

    # Convertir a un formato JSON o cualquier otro formato necesario
    resultado = [{'id': mercancia.merchant_id, 'nombre': mercancia.name, 'deleted': mercancia.deleted} for mercancia in mercancias]

    return jsonify(resultado)

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

    return jsonify({'msg': 'Obteniendo una mercancia'})

@router.route('/actualizarMercancia/<string:field>/<string:value>',  methods=['POST'])
def actualizarMercancia(field, value):
    return jsonify({'msg': 'Actualizando una mercancia'})

@router.route('/eliminarMercancia/<string:field>/<string:value>',  methods=['DELETE'])
def eliminarMercancia(field, value):
    return jsonify({'msg': 'Eliminando una mercancia'})