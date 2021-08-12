from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import CustomUser, Role, Permission, Product, Activity, Message
from .serializers import UserSerializer, RoleSerializer, PermissionSerializer, ProductSerializer, ActivitySerializer


class BasicSetPagination(PageNumberPagination):
    """
    基本的分页器。
    """
    page_size = 20
    page_query_param = 'page'
    page_size_query_param = 'size'
    max_page_size = None


class UserViewSet(viewsets.ModelViewSet):
    """
    用户通用视图集
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    pagination_class = BasicSetPagination


class RoleViewSet(viewsets.ModelViewSet):
    """
    角色通用视图集
    """
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    pagination_class = BasicSetPagination


class PermissionViewSet(viewsets.ModelViewSet):
    """
    权限通用视图集
    """
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    pagination_class = BasicSetPagination


class ProductViewSet(viewsets.ModelViewSet):
    """
    产品通用视图集
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = BasicSetPagination


class ActivityViewSet(viewsets.ModelViewSet):
    """
    活动通用视图集
    """
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    pagination_class = BasicSetPagination



