from django.db import models

class WordManager(models.Manager):
  def create_word(self, word, kor, eng):
    # if not title:
    #   raise ValueError('must have title')
    word = self.model(
      word = word,
      kor = kor,
      eng = eng
    )

    word.save()
    return word

class Word(models.Model):
  id = models.AutoField(primary_key=True)
  word = models.CharField(verbose_name="단어", max_length=50, unique=True)
  kor = models.CharField(verbose_name="한국어 뜻", max_length=50)
  eng = models.CharField(verbose_name="영어 뜻", max_length=100)

  objects = WordManager()

  def __str__(self):
    return self.word