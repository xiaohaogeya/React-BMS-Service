from rest_framework import serializers
from .models import CustomUser, Activity, Product, Permission, Role


class UserSerializer(serializers.ModelSerializer):
    """
    用户序列化器
    """

    class Meta:
        model = CustomUser
        fields = ['name', 'mobile', 'id', 'email']


class ActivitySerializer(serializers.ModelSerializer):
    """
    活动序列化器
    """

    class Meta:
        model = Activity
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    """
    产品序列化器
    """

    class Meta:
        model = Product
        fields = "__all__"


class PermissionSerializer(serializers.ModelSerializer):
    """
    权限序列化器
    """
    key = serializers.SerializerMethodField(read_only=True)

    def get_key(self, obj):
        return obj.id

    class Meta:
        model = Permission
        fields = "__all__"


class RoleSerializer(serializers.ModelSerializer):
    """
    角色序列化器
    """

    class Meta:
        model = Role
        fields = "__all__"


class PermissionTreeSerializer(serializers.ModelSerializer):
    """
    权限树序列化器
    """
    children = serializers.SerializerMethodField(read_only=True)
    key = serializers.SerializerMethodField(read_only=True)

    def get_children(self, obj):
        permissions = Permission.objects.filter(parent=obj.id)
        return PermissionSerializer(instance=permissions, many=True).data

    def get_key(self, obj):
        return obj.id

    class Meta:
        model = Permission
        fields = "__all__"
