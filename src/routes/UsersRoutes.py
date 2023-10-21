from flask import Blueprint, request, jsonify

from src.data_example.users import usuarios

router = Blueprint('usuarios_blueprint', __name__)

@router.route('/', methods=['GET'])
def obtenerUsuarios():
    return jsonify(usuarios)
