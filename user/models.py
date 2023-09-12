from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

class UserManager(BaseUserManager):
  def create(self, uid, pw):
    if (not uid):
      return "Must Have ID"
    user = self.model(
      uid = uid
    )
    user.set_password(pw)
    user.save()
    return user
  
  def create_superuser(self, uid, pw):
    admin = self.create_user(uid, pw)
    admin.isAdmin = True
    admin.save()
    return admin

class User(AbstractBaseUser):
  id = models.AutoField(primary_key=True)
  uid = models.CharField(max_length=255, verbose_name="계정", unique=True)
  isAdmin = models.BooleanField(verbose_name="권한", default=False)

  objects = UserManager()

  USERNAME_FIELD = 'uid'

  def __str__(self):
    return self.uid

