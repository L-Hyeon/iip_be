import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.db.models import Q

from core.utils import loginDecorator
from .models import Study
from .serializers import StudySerializer

from word.models import Word
from word.serializers import WordSerializer

class AddStudy(APIView):
  @loginDecorator
  def post(self, request):
    data = json.loads(request.body.decode('utf-8'))
    user = Token.objects.get(key=request.headers['Authorization']).user
    try:
      study = Study.objects.get(Q(user_id=user.id) & Q(word_id=data['wid']))
    except:
      study = Study.objects.create_study(user_id=user.id, word_id=data['wid'])
    return Response(status=200)


class DeleteStudy(APIView):
  @loginDecorator
  def delete(self, request, id):
    user = Token.objects.get(key=request.headers['Authorization']).user
    study = Study.objects.get(Q(user_id=user.id) & Q(word_id=id))
    
    if (user.id != study.user_id):
      return Response(status=401)

    study.delete()
    return Response(status=200)


class GetStudies(APIView):
  @loginDecorator
  def get(self, request, page):
    user = Token.objects.get(key=request.headers['Authorization']).user
    study = Study.objects.filter(user_id=user.id)[20*page: 20*(page + 1)]
    ret = []
    for e in study:
      word = Word.objects.get(id=e.word_id)
      ret.append({"id": word.id, "word": word.word, "kor": word.kor, "eng": word.eng})
    return Response(status=200, data=ret)

class GetAllStudies(APIView):
  @loginDecorator
  def get(self, request):
    user = Token.objects.get(key=request.headers['Authorization']).user
    study = Study.objects.filter(user_id=user.id)
    ret = list()
    for e in study:
      ret.append(e.word_id)
    return Response(status=200, data=ret)
