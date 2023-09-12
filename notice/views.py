import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from core.utils import adminDecorator, loginDecorator
from .models import Notice
from .serializers import NoticeSerializer

class AddNotice(APIView):
  @loginDecorator
  def post(self, request):
    data = json.loads(request.body.decode('utf-8'))
    user = Token.objects.get(key=request.headers['Authorization']).user
    notice = Notice.objects.create_notice(title=data['title'], content=data['content'], uid=user.uid)
    return Response(status=200, data=NoticeSerializer(notice).data)


class ModifyNotice(APIView):
  @loginDecorator
  def post(self, request, id):
    data = json.loads(request.body.decode('utf-8'))
    notice = Notice.objects.get(id=id)
    user = Token.objects.get(key=request.headers['Authorization']).user
    if (not (user.uid == notice.uid or user.isAdmin)):
      return Response(status=401)

    notice.title = data['title']
    notice.content = data['content']
    notice.save()
    return Response(status=200, data=NoticeSerializer(notice).data)


class DeleteNotice(APIView):
  @loginDecorator
  def delete(self, request, id):
    try:
      notice = Notice.objects.get(id=id)
    except:
      return Response(status=401)
    user = Token.objects.get(key=request.headers['Authorization']).user
    if (not (user.uid == notice.uid or user.isAdmin)):
      return Response(status=401)
    notice.delete()
    return Response(status=200)


class GetNotice(APIView):
  def get(self, request, id):
    notice = Notice.objects.get(id=id)
    return Response(status=200, data=NoticeSerializer(notice).data)


class GetNotices(APIView):
  def get(self, request, page):
    notice = Notice.objects.all()[20*page: 20*(page + 1)]
    return Response(status=200, data=NoticeSerializer(notice, many=True).data)
