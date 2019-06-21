from django.contrib.auth.models import Permission
from rest_framework import serializers


# 用于权限的查询创建
class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'
