from datetime import datetime
from django.db import models

class NoticeManager(models.Manager):
  def create_notice(self, title, content, uid):
    notice = self.model(
      title = title,
      content = content,
      createtime = datetime.now(),
      uid = uid
    )
    notice.save()
    return notice

class Notice(models.Model):
  id = models.AutoField(primary_key=True)
  title = models.CharField(verbose_name="제목", max_length=255)
  content = models.TextField(verbose_name="내용")
  uid = models.CharField(verbose_name="작성자", max_length=255)
  createtime = models.DateTimeField(verbose_name="작성일시", default=datetime.now())

  objects = NoticeManager()

  def __str__(self):
    return self.title