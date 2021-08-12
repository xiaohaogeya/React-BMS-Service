from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.timezone import now as timezoneNow


class BaseModel(models.Model):
    """
    基础model
    """
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # 本类不去生成数据库的表


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, name, email=None, password=None, **extra_fields):
        if not name:
            raise ValueError("Users must have an name")
        email = self.normalize_email(email)
        username = self.model.normalize_username(name)
        user = self.model(name=username,
                          email=email,
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, password):
        user = self.create_user(
            name,
            password=password,
        )
        user.is_admin = True
        user.is_back_admin = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, BaseModel):
    """
    用户信息
    """
    roles = models.ManyToManyField('Role', blank=True)
    name = models.CharField(max_length=50, unique=True, verbose_name='用户名称')
    avatar = models.CharField(max_length=200, verbose_name='用户头像')
    mobile = models.CharField(max_length=20, blank=True, null=True, verbose_name='用户手机号')
    email = models.CharField(max_length=32, blank=True, null=True, verbose_name='用户邮箱')

    is_admin = models.BooleanField(default=False, verbose_name='是否是管理员')
    is_back_admin = models.BooleanField(default=False, verbose_name='是否是后台管理员')

    objects = CustomUserManager()

    USERNAME_FIELD = "name"

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.name

    @property
    def is_staff(self):
        return self.is_admin

    @property
    def is_back_staff(self):
        return self.is_back_admin

    class Meta:
        verbose_name = '用户表(CustomUser)'
        verbose_name_plural = verbose_name


class Activity(BaseModel):
    """
    活动
    """
    title = models.CharField(max_length=50, unique=True, verbose_name='活动名称')
    description = models.CharField(max_length=200, blank=True, null=True, verbose_name='活动描述')
    start_time = models.DateTimeField(default=timezoneNow, verbose_name='开始时间')
    end_time = models.DateTimeField(default=timezoneNow, verbose_name='结束时间')

    class Meta:
        verbose_name = '活动表(Activity)'
        verbose_name_plural = verbose_name


class Product(BaseModel):
    """
    产品
    """
    title = models.CharField(max_length=50, unique=True, verbose_name='活动名称')
    description = models.CharField(max_length=200, blank=True, null=True, verbose_name='活动描述')

    class Meta:
        verbose_name = '产品表(Product)'
        verbose_name_plural = verbose_name


class Message(BaseModel):
    """
    消息
    """
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, verbose_name='标题')
    content = models.CharField(max_length=300, verbose_name='内容')

    class Meta:
        verbose_name = '消息表(Message)'
        verbose_name_plural = verbose_name


class Role(BaseModel):
    """
    角色
    """
    permissions = models.ManyToManyField('Permission', blank=True)
    name = models.CharField(max_length=32, verbose_name='角色名称')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '角色表(Role)'
        verbose_name_plural = verbose_name


class Permission(BaseModel):
    """
    权限
    """
    api_path = models.CharField(max_length=300, verbose_name='路由地址')
    rule = models.CharField(max_length=300, verbose_name='规则')
    method = models.CharField(max_length=300, verbose_name='规则')
    title = models.CharField(max_length=300, verbose_name='规则')
    parent = models.ForeignKey('self', null=True, blank=True, verbose_name='二级菜单及权限', on_delete=models.CASCADE)
    is_menu = models.PositiveSmallIntegerField(default=1)  # 1-一级菜单/2-二级菜单以此类推
    path = models.CharField(max_length=300, verbose_name='地址')

    def __str__(self):
        return self.title
