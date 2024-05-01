from flask import Blueprint, request, jsonify
from ..services.AuthService import AuthService

router = Blueprint('auth_blueprint', __name__)
@router.route('/login',  methods=['POST'])
def login():
    datos_usuario = request.json
    print(datos_usuario)
    token = AuthService.login(datos_usuario)
    if token != None:
        return jsonify({'token': token})
    else:
        return jsonify({'error': 'Error de inicio de sesión'})


@router.route('/device',  methods=['POST'])
def loginDevice():
    datos_dispositivo = request.json
    print(datos_dispositivo)
    token = AuthService.loginDevice(datos_dispositivo)
    if token != None:
        return jsonify({'token': token})
    else:
        return jsonify({'error': 'Error de inicio de sesión'})