from ..models.UserModel import UserModel
from ..models.DevicesModel import  DevicesModel
from ..utils.SecurityUtils import Security
class AuthService():
    @classmethod
    def login(cls, user):
        query = {
            'username' : user['username'],
            'password' : user['pass']
        }

        usuario = UserModel.query.filter_by(**query).first()
        print(usuario)
        if usuario:
            token = Security.generar_token(usuario)
            print('token:')
            print(token)
            return token
        else:
            return None

    @classmethod
    def loginDevice(cls, device):
        query = {
            'username': device['name'],
            'password': device['password']
        }

        dispositivo = DevicesModel.query.filter_by(**query).first()
        print(dispositivo)
        if dispositivo:
            token = Security.generar_token_dispositivo(dispositivo)
            print('token:')
            print(token)
            return token
        else:
            return None