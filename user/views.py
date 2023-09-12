import json
from django.contrib import auth
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from core.utils import loginDecorator, adminDecorator
from .models import User
from .serializers import UserSerializer

from study.models import Study


class Register(APIView):
  def post(self, request):
    data = json.loads(request.body.decode('utf-8'))
    try:
      user = User.objects.get(uid=data['uid'])
    except:
      user = User.objects.create(
        uid=data["uid"],
        pw=data['pw']
      )
    token = Token.objects.create(user=user)
    return Response(status=200, data={"Token": token.key, "isAdmin": user.isAdmin, "uid": user.uid})


class Login(APIView):
  def post(self, request):
    data = json.loads(request.body)
    user = auth.authenticate(username=data["uid"], password=data["pw"])
    if (user is not None):
      token = Token.objects.get(user=user)
      if (token is None):
        token = Token.objects.create(user=user)
      return Response(status=200, data={"Token": token.key, "isAdmin": user.isAdmin, "uid": user.uid})
    else:
      return Response(status=401)


class Logout(APIView):
  @loginDecorator
  def get(self, request):
    token = request.headers['Authorization']
    hasToken = Token.objects.get(key=token)
    hasToken.delete()
    return Response({"Logout"})


class Changepw(APIView):
  @loginDecorator
  def post(self, request):
    data = json.loads(request.body)
    newpw = data["newpw"]
    
    user = Token.objects.get(key=request.headers['Authorization']).user
    user.set_password(newpw)
    user.save()

    # Change Token
    token = Token.objects.get(user=user)
    token.delete()
    token = Token.objects.create(user=user)
    return Response({"Token": token.key})


class GetUser(APIView):
  def get(self, request, id):
    target = User.objects.get(id=id)
    return Response(UserSerializer(target).data)


class GetUsers(APIView):
  @adminDecorator
  def get(self, request, page):
    target = User.objects.all()[20*page: 20*(page + 1)]
    return Response(UserSerializer(target, many=True).data)


class DeleteUser(APIView):
  @adminDecorator
  def delete(self, request, id):
    user = Token.objects.get(key=request.headers['Authorization']).user
    if (user is None):
      return Response(status=404)
    if (user.id == id):
        st = Study.objects.filter(user_id=user.id)
        for e in st:
          e.delete()
        user.delete()
        return Response(status=200)
    elif (user.isAdmin):
      user = User.objects.get(id=id)
      st = Study.objects.filter(user_id=id)
      for e in st:
        e.delete()
      user.delete()
      return Response(status=200)
    else:
        return Response(status=403)
