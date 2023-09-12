import json
from rest_framework.views import APIView
from rest_framework.response import Response

from core.utils import adminDecorator
from .models import Word
from .serializers import WordSerializer


class AddWord(APIView):
  @adminDecorator
  def post(self, request):
    data = json.loads(request.body.decode('utf-8'))
    try:
      word = Word.objects.get(word=data['word'])
    except:
      word = Word.objects.create_word(data['word'], data['kor'], data['eng'])
    return Response(status=200, data=WordSerializer(word).data)

class ModifyWord(APIView):
  @adminDecorator
  def post(self, request, id):
    data = json.loads(request.body.decode('utf-8'))
    word = Word.objects.get(id=id)
    if (word is None):
      return Response(404)
    word.word = data['word']
    word.kor = data['kor']
    word.eng = data['eng']
    word.save()
    return Response(status=200, data=WordSerializer(word).data)

class DeleteWord(APIView):
  @adminDecorator
  def delete(self, request, id):
    word = Word.objects.get(id=id)
    if (word is None):
      return Response(status=404)
    word.delete()
    return Response(status=200)
  

class GetWord(APIView):
  def get(self, request, id):
    word = Word.objects.get(id=id)
    if (word is None):
      return Response(status=404)
    return Response(data=WordSerializer(word).data)


class GetWords(APIView):
  def get(self, request, page):
    target = Word.objects.all()[::-1][20*page: 20*(page + 1)]
    return Response(data=WordSerializer(target, many=True).data)
