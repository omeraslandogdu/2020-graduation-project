from rest_framework.authentication import TokenAuthentication

from applications.recognition.models import ClientToken


class ClientTokenAuthentication(TokenAuthentication):
    model = ClientToken
