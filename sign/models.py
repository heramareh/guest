from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
'''
class UserProfile(models.Model):
    user = models.OneToOneField(User, None)
    desc = models.TextField()
'''
class User(AbstractUser):
    desc = models.TextField()
    # password = models.CharField(max_length=128)
    # last_login = models.DateTimeField(auto_now=True)
    # is_superuser = models.TextField(max_length=1)
    # username = models.CharField(max_length=150,unique=True)
    # first_name = models.CharField(max_length=30)
    # last_name = models.CharField(max_length=150)
    # email = models.EmailField()
    # is_staff = models.BooleanField()
    # is_active = models.BooleanField()
    # date_joined = models.DateTimeField()
    #
    # def __str__(self):
    #     return self.username

# 发布会表
class Event(models.Model):
    # 发布会标题
    name = models.CharField(max_length=100)
    # 参加人数
    limit = models.IntegerField()
    # 状态
    status = models.BooleanField()
    # 地址
    address = models.CharField(max_length=200)
    # 发布会时间
    start_time = models.DateTimeField('events time')
    # 创建时间（自动获取当前时间）
    create_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Guest(models.Model):
    # 关联发布会id
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    # 姓名
    realname = models.CharField(max_length=64)
    # 手机号
    phone = models.CharField(max_length=16)
    # 邮箱
    email = models.EmailField()
    # 签到状态
    sign = models.BooleanField()
    # 创建时间（自动获取当前时间）
    create_time = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("event", "phone")

    def __str__(self):
      return self.realname
