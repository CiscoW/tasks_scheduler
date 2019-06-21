from django.contrib.auth.models import User
from rest_framework import serializers


# 用于查询，修改用户信息(不包括密码)、删除用户
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'  # ('id', 'username', 'email', 'is_superuser', 'is_staff', 'is_active', 'date_joined')
        exclude = ('password',)


# 用于新增用户和修改用户密码
class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def validate(self, data):
        """
        自定义验证规则
        """
        if len(data['password']) < 4:
            raise serializers.ValidationError("密码长度过短")

        return data


class UpdateUserPasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(max_length=128)
    new_password = serializers.CharField(max_length=128)

    class Meta:
        model = User
        fields = ('old_password', 'new_password')

    def update(self, instance, validated_data):
        if instance.check_password(validated_data.pop('old_password')):
            setattr(instance, 'old_password', instance.password)
            instance.set_password(validated_data.pop('new_password'))
            instance.save()
            # 返回结果会按 fields 中内容展示
            setattr(instance, 'new_password', instance.password)
            return instance
        else:
            raise serializers.ValidationError("原密码错误")
