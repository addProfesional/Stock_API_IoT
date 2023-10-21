from flask import Blueprint, request, jsonify

router = Blueprint('mercancias_blueprint', __name__)

@router.route('/', methods=['GET'])
def obtenerMercancias():
    return jsonify({ 'msg': 'Obteniendo las mercancías'})