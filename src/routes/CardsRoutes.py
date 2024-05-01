from flask import Blueprint, request, jsonify
from ..models.CardsModel import CardsModel
from ..database.Database import db
from ..utils.SecurityUtils import Security

router = Blueprint('cards_blueprint', __name__)

@router.before_request
def verificar_token():
    tiene_acceso = Security.verificar_token(request.headers)
    if not tiene_acceso: return jsonify({'error': 'No está autorizado para realizar la petición'}), 401
@router.route('/',  methods=['GET'])
def obtenerCards():
    # Obtener usuarios desde la base de datos utilizando el modelo
    cards = CardsModel.query.all()

    # Convertir a un formato JSON o cualquier otro formato necesario
    resultado = [{'id': card.card_id, 'uuid_card': card.uuid_card} for card in cards]

    return jsonify(resultado), 200

@router.route('/crear',  methods=['POST'])
def crearCard():
    datos_json = request.json

    # Crear una instancia del modelo a partir de los datos JSON
    nuevo_card = CardsModel.crear_desde_json(datos_json)
    print(nuevo_card)

    # Agregar la nueva instancia a la base de datos y hacer commit
    db.session.add(nuevo_card)
    db.session.commit()

    return jsonify({'msg': {'id': nuevo_card.card_id, 'uuid_card': nuevo_card.uuid_card}})
    # return jsonify({'msg': 'Creando dispositivo'})

@router.route('/obtenerCard/<string:field>/<string:value>',  methods=['GET'])
def obtenerCard(field, value):
    # Validar que el campo sea uno de los campos válidos del modelo Usuario
    campos_validos = [columna.name for columna in CardsModel.__table__.columns]
    if field not in campos_validos:
        return jsonify({'error': 'Campo no válido'}), 400

    # Construir la consulta dinámica
    filtro = {field: value}
    print(filtro)
    card = CardsModel.query.filter_by(**filtro).first()
    print(card)

    if card:
        resultado = {
            'id': card.device_id,
            'uuid_card': card.uuid_card,
            'type': card.type
        }
        return jsonify(resultado), 200
    else:
        return jsonify({'error': 'Dispositivo no encontrado'}), 404

@router.route('/actualizarCard/<string:field>/<string:value>',  methods=['POST'])
def actualizarCard(field, value):
    datos_json = request.json

    # Validar que el campo sea uno de los campos válidos del modelo Usuario
    campos_validos = [columna.name for columna in CardsModel.__table__.columns]
    if field not in campos_validos:
        return jsonify({'error': 'Campo no válido'}), 400

    # Construir la consulta dinámica
    filtro = {field: value}
    print(filtro)
    card = CardsModel.query.filter_by(**filtro).first()
    print(card)

    card.uuid_card = datos_json['name']
    card.type = datos_json['type']
    # Agregar campos que hagan falta

    db.session.commit()

    return jsonify({'msg': 'Dispositivo ' +str(card.card_id)+ ' actualizado' }), 200

@router.route('/eliminarCard/<string:field>/<string:value>',  methods=['DELETE'])
def eliminarCard(field, value):
    # Validar que el campo sea uno de los campos válidos del modelo Usuario
    campos_validos = [columna.name for columna in CardsModel.__table__.columns]
    if field not in campos_validos:
        return jsonify({'error': 'Campo no válido'}), 400

    # Construir la consulta dinámica
    filtro = {field: value}
    print(filtro)
    card = CardsModel.query.filter_by(**filtro).first()
    print(card)

    db.session.delete(card)
    db.session.commit()

    return jsonify({'msg': 'Dispositivo ' +str(card.card_id)+ ' eliminado'}), 200