import jwt
import time 
from config import get_settings

settings = get_settings()

def decodeJWT(token:str) -> dict:
    try:
        decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        return decoded_token if decoded_token['exp'] >= time.time() else None
    except jwt.ExpiredSignatureError:
        print("Token has expired.")
    except jwt.InvalidTokenError as e:
        print("Error decoding token:", str(e))
    return None
