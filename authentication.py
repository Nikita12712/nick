import jwt
import datetime
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return None

        try:
            token = auth_header.split(" ")[1]
            payload = jwt.decode(
                token,
                settings.JWT_SECRET_KEY,
                algorithms=["HS256"]
            )
        except (jwt.ExpiredSignatureError, jwt.DecodeError):
            raise AuthenticationFailed("Токен недійсний або закінчився.")

        try:
            user = User.objects.get(id=payload['user_id'])
        except User.DoesNotExist:
            raise AuthenticationFailed("Користувач не знайдений.")

        return (user, None)

    @staticmethod
    def generate_tokens(user):
        access_payload = {
            'user_id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=settings.JWT_ACCESS_TOKEN_LIFETIME),
            'type': 'access'
        }

        refresh_payload = {
            'user_id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=settings.JWT_REFRESH_TOKEN_LIFETIME),
            'type': 'refresh'
        }

        access_token = jwt.encode(access_payload, settings.JWT_SECRET_KEY, algorithm='HS256')
        refresh_token = jwt.encode(refresh_payload, settings.JWT_SECRET_KEY, algorithm='HS256')

        return {
            'access': access_token,
            'refresh': refresh_token
        }

    @staticmethod
    def refresh_token(refresh_token):
        try:
            payload = jwt.decode(
                refresh_token,
                settings.JWT_SECRET_KEY,
                algorithms=["HS256"]
            )
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Рефреш токен закінчився.")
        except jwt.DecodeError:
            raise AuthenticationFailed("Неправильний токен.")

        if payload['type'] != 'refresh':
            raise AuthenticationFailed("Недійсний тип токену.")

        user = User.objects.get(id=payload['user_id'])

        return JWTAuthentication.generate_tokens(user)