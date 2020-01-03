from django.contrib import admin

# Register your models here.

from board.models import Table1
admin.site.register(Table1)


# pip 버전 확인후 아래보다 상위버전이면 다운그레이드 
# django 2.2.5로변경 

# $python manage.py createsuperuser
# 아이디 admin 
# 비번 1234
