from flask import Blueprint, request, jsonify, abort
from ..models.UserModel import UserModel
from ..database.Database import db
from ..utils.SecurityUtils import Security

router = Blueprint('usuarios_blueprint', __name__)

@router.before_request
def verificar_token():
    tiene_acceso = Security.verificar_token(request.headers)
    if not tiene_acceso: return jsonify({'error': 'No está autorizado para realizar la petición'}), 401

@router.route('/', methods=['GET'])
def obtenerUsuarios():
    # Obtener usuarios desde la base de datos utilizando el modelo
    usuarios = UserModel.query.all()

    # Convertir a un formato JSON o cualquier otro formato necesario
    resultado = [{'id': usuario.user_id, 'nombre': usuario.name} for usuario in usuarios]

    return jsonify(resultado)
@router.route('/crear',  methods=['POST'])
def crearUsuario():
    datos_json = request.json

    # Crear una instancia del modelo a partir de los datos JSON
    nuevo_usuario = UserModel.crear_desde_json(datos_json)
    print(nuevo_usuario)

    # Agregar la nueva instancia a la base de datos y hacer commit
    db.session.add(nuevo_usuario)
    db.session.commit()

    return jsonify({'msg': {'id': nuevo_usuario.user_id, 'nombre': nuevo_usuario.name}})

@router.route('/obtenerUsuario/<string:field>/<string:value>',  methods=['GET'])
def obtenerUsuario(field, value):

    # Validar que el campo sea uno de los campos válidos del modelo Usuario
    campos_validos = [columna.name for columna in UserModel.__table__.columns]
    if field not in campos_validos:
        return jsonify({'error': 'Campo no válido'}), 400

    # Construir la consulta dinámica
    filtro = {field: value}
    print(filtro)
    usuario = UserModel.query.filter_by(**filtro).first()
    print(usuario)

    if usuario:
        resultado = {
            'id': usuario.user_id,
            'name' : usuario.name,
            'email' : usuario.email
        }
        return jsonify(resultado)
    else:
        return jsonify({'error': 'Usuario no encontrado'}), 404


@router.route('/actualizarUsuario/<string:field>/<string:value>',  methods=['POST'])
def actualizarUsuario(field, value):
    datos_json = request.json
    campos_validos = [columna.name for columna in UserModel.__table__.columns]
    if field not in campos_validos:
        return jsonify({'error': 'Campo no válido'}), 400

    # Construir la consulta dinámica
    filtro = {field: value}
    print(filtro)
    usuario = UserModel.query.filter_by(**filtro).first()
    print(usuario)

    usuario.name = datos_json['name']
    usuario.username = datos_json['username']
    usuario.email = datos_json['email']

    db.session.commit()

    return jsonify({'msg': 'Usuario ' +str(usuario.user_id)+ ' actualizado' }), 200

@router.route('/eliminarUsuario/<string:field>/<string:value>',  methods=['DELETE'])
def eliminarUsuario(field, value):
    # Validar que el campo sea uno de los campos válidos del modelo Usuario
    campos_validos = [columna.name for columna in UserModel.__table__.columns]
    if field not in campos_validos:
        return jsonify({'error': 'Campo no válido'}), 400

    # Construir la consulta dinámica
    filtro = {field: value}
    print(filtro)
    usuario = UserModel.query.filter_by(**filtro).first()
    print(usuario)

    db.session.delete(usuario)
    db.session.commit()

    return jsonify({'msg': 'Usuario ' +str(usuario.user_id)+ ' eliminado'})