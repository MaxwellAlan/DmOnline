from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserInfo(models.Model):
    user = models.OneToOneField(User, unique=True)
    phone = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=100,null=True)

    def __str__(self):
        return 'user {}'.format(self.user.username)