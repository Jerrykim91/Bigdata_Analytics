#from django.db import models

# Create your models here.


from django.db import models

class Table1(models.Model):
    objects  = models.Manager() #vs code 오류 제거용

    no      = models.AutoField(primary_key=True)
    title   = models.CharField(max_length=200)
    content = models.TextField() 
    writer  = models.CharField(max_length=50)
    hit     = models.IntegerField()
    img     = models.BinaryField(null = True)
    regdate = models.DateTimeField(auto_now_add=True)

# 이거 테이블 추가 할때마다 생성 
# $ python manage.py check
# $ python manage.py makemigrations board
#  필수인가 ?
# $ python manage.py migrate board