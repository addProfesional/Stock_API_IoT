from flask import Blueprint, request, jsonify
from ..models.UserModel import UserModel
from ..database.Database import db

router = Blueprint('usuarios_blueprint', __name__)

@router.route('/', methods=['GET'])
def obtenerUsuarios():
    # Obtener usuarios desde la base de datos utilizando el modelo
    usuarios = UserModel.query.all()

    # Convertir a un formato JSON o cualquier otro formato necesario
    resultado = [{'id': usuario.user_id, 'nombre': usuario.nombre} for usuario in usuarios]

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
    return jsonify({'msg': 'Obteniendo un usuario'})

@router.route('/actualizarUsuario/<string:field>/<string:value>',  methods=['POST'])
def actualizarUsuario(field, value):
    return jsonify({'msg': 'Actualizando un usuario'})

@router.route('/eliminarUsuario/<string:field>/<string:value>',  methods=['DELETE'])
def eliminarUsuario(field, value):
    return jsonify({'msg': 'Eliminando un usuario'})