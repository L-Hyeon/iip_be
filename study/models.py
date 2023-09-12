from django.db import models

class StudyManager(models.Manager):
  def create_study(self, user_id, word_id):
    study = self.model(
      user_id = user_id,
      word_id = word_id
    )
    study.save()
    return study

class Study(models.Model):
  id = models.AutoField(primary_key=True)
  user_id = models.IntegerField(verbose_name="유저")
  word_id = models.IntegerField(verbose_name="단어")

  objects = StudyManager()
