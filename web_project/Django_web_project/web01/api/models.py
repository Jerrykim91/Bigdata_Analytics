# api/models.py

from django.db import models

#################################################

# 이거 테이블 추가 할때마다 생성 
# $ python manage.py check
# $ python manage.py makemigrations member
# 필수
# $ python manage.py migrate member

#################################################

# Create your models here.
# 테이블 생성시 앱명_테이블네임이랑 보드랑 중복되도 괜찮음 

class Item(models.Model):
    objects  = models.Manager() 

    no         = models.AutoField(primary_key=True)
    name       = models.CharField(max_length=30)
    price      = models.IntegerField()
    regdate    = models.DateTimeField(auto_now_add=True)