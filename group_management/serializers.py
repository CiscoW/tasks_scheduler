from django.contrib.auth.models import Group
from rest_framework import serializers


# 用于组的查询创建
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
