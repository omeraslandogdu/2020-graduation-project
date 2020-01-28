from rest_framework.authentication import TokenAuthentication

from applications.recognition.models import UserToken


class UserTokenAuthentication(TokenAuthentication):
    model = UserToken
