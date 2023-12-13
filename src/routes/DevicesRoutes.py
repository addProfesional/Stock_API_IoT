from flask import Blueprint, request, jsonify
from ..models.DevicesModel import DevicesModel
from ..database.Database import db
from ..utils.SecurityUtils import Security

router = Blueprint('devices_blueprint', __name__)

@router.before_request
def verificar_token():
    tiene_acceso = Security.verificar_token(request.headers)
    if not tiene_acceso: return jsonify({'error': 'No está autorizado para realizar la petición'}), 401
@router.route('/',  methods=['GET'])
def obtenerDispositivos():
    # Obtener usuarios desde la base de datos utilizando el modelo
    dispositivos = DevicesModel.query.all()

    # Convertir a un formato JSON o cualquier otro formato necesario
    resultado = [{'id': dispositivo.device_id, 'nombre': dispositivo.name} for dispositivo in dispositivos]

    return jsonify(resultado), 200

@router.route('/crear',  methods=['POST'])
def crearDispositivo():
    datos_json = request.json

    # Crear una instancia del modelo a partir de los datos JSON
    nuevo_dispositivo = DevicesModel.crear_desde_json(datos_json)
    print(nuevo_dispositivo)

    # Agregar la nueva instancia a la base de datos y hacer commit
    db.session.add(nuevo_dispositivo)
    db.session.commit()

    return jsonify({'msg': {'id': nuevo_dispositivo.device_id, 'nombre': nuevo_dispositivo.name}})
    # return jsonify({'msg': 'Creando dispositivo'})

@router.route('/obtenerDispositivo/<string:field>/<string:value>',  methods=['GET'])
def obtenerDispositivo(field, value):
    # Validar que el campo sea uno de los campos válidos del modelo Usuario
    campos_validos = [columna.name for columna in DevicesModel.__table__.columns]
    if field not in campos_validos:
        return jsonify({'error': 'Campo no válido'}), 400

    # Construir la consulta dinámica
    filtro = {field: value}
    print(filtro)
    dispositivo = DevicesModel.query.filter_by(**filtro).first()
    print(dispositivo)

    if dispositivo:
        resultado = {
            'id': dispositivo.device_id,
            'name': dispositivo.name,
            'type': dispositivo.type
        }
        return jsonify(resultado), 200
    else:
        return jsonify({'error': 'Dispositivo no encontrado'}), 404

@router.route('/actualizarDispositivo/<string:field>/<string:value>',  methods=['POST'])
def actualizarDispositivo(field, value):
    datos_json = request.json

    # Validar que el campo sea uno de los campos válidos del modelo Usuario
    campos_validos = [columna.name for columna in DevicesModel.__table__.columns]
    if field not in campos_validos:
        return jsonify({'error': 'Campo no válido'}), 400

    # Construir la consulta dinámica
    filtro = {field: value}
    print(filtro)
    dispositivo = DevicesModel.query.filter_by(**filtro).first()
    print(dispositivo)

    dispositivo.name = datos_json['name']
    dispositivo.type = datos_json['type']
    # Agregar campos que hagan falta

    db.session.commit()

    return jsonify({'msg': 'Dispositivo ' +str(dispositivo.device_id)+ ' actualizado' }), 200

@router.route('/eliminarDispositivo/<string:field>/<string:value>',  methods=['DELETE'])
def eliminarDispositivo(field, value):
    # Validar que el campo sea uno de los campos válidos del modelo Usuario
    campos_validos = [columna.name for columna in DevicesModel.__table__.columns]
    if field not in campos_validos:
        return jsonify({'error': 'Campo no válido'}), 400

    # Construir la consulta dinámica
    filtro = {field: value}
    print(filtro)
    dispositivo = DevicesModel.query.filter_by(**filtro).first()
    print(dispositivo)

    db.session.delete(dispositivo)
    db.session.commit()

    return jsonify({'msg': 'Dispositivo ' +str(dispositivo.device_id)+ ' eliminado'}), 200