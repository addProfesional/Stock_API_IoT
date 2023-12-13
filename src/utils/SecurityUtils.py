import datetime
import jwt
import pytz
from dotenv import load_dotenv
# from flask_jwt_extended import create_access_token
import os

load_dotenv('.env.dev')
class Security:
    key_secret = os.environ.get('JWT_KEY')
    tz = pytz.timezone('America/Mexico_City')

    @classmethod
    def generar_token(cls, usuario_autenticado):
        payload = {
            'iat': datetime.datetime.now(tz=cls.tz),
            'exp': datetime.datetime.now(tz=cls.tz) + datetime.timedelta(minutes=10),
            'username' : usuario_autenticado.username
        }

        return jwt.encode(payload, cls.key_secret, algorithm="HS256")

    @classmethod
    def verificar_token(cls, headers):
        if 'Authorization' in headers.keys():
            authorization = headers['Authorization']
            print(authorization)
            encoded_token = authorization.split(' ')[1]
            print(encoded_token)
            try:
                payload = jwt.decode(encoded_token, cls.key_secret, algorithms=['HS256'])
                print(payload)
                return True
            except (jwt.ExpiredSignatureError, jwt.InvalidSignatureError):
                return False
        return False