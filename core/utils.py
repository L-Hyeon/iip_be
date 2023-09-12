from rest_framework.authtoken.models import Token
from rest_framework.response import Response


def loginDecorator(func):
    def wrapper(self, request, *args, **kwargs):
        token = Token.objects.get(key=request.headers['Authorization'])
        if (token is None):
            return Response(status=401, data={"Access Denied"})
        return func(self, request, *args, **kwargs)
    return wrapper

def adminDecorator(func):
    def wrapper(self, request, *args, **kwargs):
        token = Token.objects.get(key=request.headers['Authorization'])
        if (token is None):
            return Response(status=401, data={"Access Denied"})
        user = token.user
        if (not user.isAdmin):
            return Response(status=401, data={"Access Denied"})
        return func(self, request, *args, **kwargs)
    return wrapper