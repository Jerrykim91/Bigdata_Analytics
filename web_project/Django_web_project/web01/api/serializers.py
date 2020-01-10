# serializers.py => 직렬화 

from rest_framework import serializers
# 모델 호출 
from.models import Item

class ItemSerializers(Serializers.ModelSerializers):
    class Meta:
        model = Item
        fields = ('no', 'name', 'price', 'regdate')
        