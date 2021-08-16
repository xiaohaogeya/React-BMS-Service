# coding=utf-8
from django.conf.urls import url, include
from rest_framework import routers
from .views import UserViewSet, ActivityViewSet, ProductViewSet, PermissionViewSet, RoleViewSet, UserLoginView, \
    PermissionTreeView, UserInfoView, QueryUserPermissionView

router = routers.DefaultRouter()

router.register(r'user', UserViewSet)
router.register(r'activity', ActivityViewSet)
router.register(r'product', ProductViewSet)
router.register(r'permission', PermissionViewSet)
router.register(r'role', RoleViewSet)
router.register(r'permission_tree', PermissionTreeView)
urlpatterns = [
    url(r'^', include(router.urls)),

    url(r'login/', UserLoginView.as_view()),
    url(r'permission_tree/', PermissionTreeView.as_view({'get': 'list'})),
    url(r'user_info', UserInfoView.as_view()),
    url(r'query_user_permissions', QueryUserPermissionView.as_view()),
]
