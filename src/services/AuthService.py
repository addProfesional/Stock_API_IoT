from ..models.UserModel import UserModel
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