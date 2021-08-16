from datetime import datetime
from django.utils import timezone
from rest_framework import viewsets, status, permissions
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework_jwt.settings import api_settings
from .models import CustomUser, Role, Permission, Product, Activity, Message
from .serializers import UserSerializer, RoleSerializer, PermissionSerializer, ProductSerializer, ActivitySerializer, \
    PermissionTreeSerializer
from .err_msg import ErrMsg


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


def jwt_response(user):
    """jwt自定义响应载荷"""
    jwt_dict = {"username": user.name, "mobile": user.mobile, "user_id": user.id}
    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
    payload = jwt_payload_handler(user)
    jwt_dict['token'] = jwt_encode_handler(payload)
    return jwt_dict


class UserLoginView(CreateAPIView):
    """
    用户登录视图集
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        print('登录的用户名:', username)
        print('登录的密码:', password)

        if not all([username, password]):
            return Response(ErrMsg().get('000001'))

        # 如果在本地系统已有账户
        user = CustomUser.objects.filter(name=username).first()

        if not user:
            return Response(ErrMsg().get('000002'))

        if user and user.check_password(password):
            user.last_login = timezone.now()
            user.save()
            return Response(ErrMsg({'results': jwt_response(user)}).get())

        return Response(ErrMsg().get('000003'))


class PermissionTreeView(viewsets.ModelViewSet):
    """
    权限树
    """
    queryset = Permission.objects.filter(parent__isnull=True)
    serializer_class = PermissionTreeSerializer


class UserInfoView(APIView):
    """
    用户信息
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user_id = self.request.user.id
        user = CustomUser.objects.filter(id=user_id).first()
        if not user:
            return Response(ErrMsg().get('000004'))

        user_data = UserSerializer(instance=user, many=False).data
        return Response(ErrMsg({'results': user_data}).get())


class QueryUserPermissionView(APIView):
    """
    获取用户权限
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user_id = self.request.user.id
        user_permissions_ids = CustomUser.objects.filter(id=user_id).values_list('roles__permissions__id', flat=True)
        permissions = Permission.objects.filter(id__in=user_permissions_ids)
        permissions_data = PermissionSerializer(instance=permissions, many=True).data
        return Response(ErrMsg({'results': permissions_data}).get())





