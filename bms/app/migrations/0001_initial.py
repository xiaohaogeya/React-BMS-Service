# Generated by Django 3.2.6 on 2021-08-12 15:52

import app.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='活动名称')),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='活动描述')),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='开始时间')),
                ('end_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='结束时间')),
            ],
            options={
                'verbose_name': '活动表(Activity)',
                'verbose_name_plural': '活动表(Activity)',
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='用户名称')),
                ('avatar', models.CharField(max_length=200, verbose_name='用户头像')),
                ('mobile', models.CharField(blank=True, max_length=20, null=True, verbose_name='用户手机号')),
                ('email', models.CharField(blank=True, max_length=32, null=True, verbose_name='用户邮箱')),
                ('is_admin', models.BooleanField(default=False, verbose_name='是否是管理员')),
                ('is_back_admin', models.BooleanField(default=False, verbose_name='是否是后台管理员')),
            ],
            options={
                'verbose_name': '用户表(CustomUser)',
                'verbose_name_plural': '用户表(CustomUser)',
            },
            managers=[
                ('objects', app.models.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('api_path', models.CharField(max_length=300, verbose_name='路由地址')),
                ('rule', models.CharField(max_length=300, verbose_name='规则')),
                ('method', models.CharField(max_length=300, verbose_name='规则')),
                ('title', models.CharField(max_length=300, verbose_name='规则')),
                ('is_menu', models.PositiveSmallIntegerField(default=1)),
                ('path', models.CharField(max_length=300, verbose_name='地址')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.permission', verbose_name='二级菜单及权限')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='活动名称')),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='活动描述')),
            ],
            options={
                'verbose_name': '产品表(Product)',
                'verbose_name_plural': '产品表(Product)',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=32, verbose_name='角色名称')),
                ('permissions', models.ManyToManyField(blank=True, to='app.Permission')),
            ],
            options={
                'verbose_name': '角色表(Role)',
                'verbose_name_plural': '角色表(Role)',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('content', models.CharField(max_length=300, verbose_name='内容')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.customuser')),
            ],
            options={
                'verbose_name': '消息表(Message)',
                'verbose_name_plural': '消息表(Message)',
            },
        ),
        migrations.AddField(
            model_name='customuser',
            name='roles',
            field=models.ManyToManyField(blank=True, to='app.Role'),
        ),
    ]
