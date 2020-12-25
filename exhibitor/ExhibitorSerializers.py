#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@author:
@contact:
@file:ExhibitorSerializers.py
@time:2020/12/21 0021 20:00
"""
from abc import ABC, ABCMeta

from django.contrib.auth.hashers import make_password, check_password
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from exhibitor.models import Exhibitors


class RegisterSerializer(ModelSerializer):
    class Meta:
        model = Exhibitors
        fields = '__all__'

    password = serializers.CharField(min_length=6, max_length=100,
                                     error_messages={
                                         'min_length': '密码不能少于6位'
                                     })
    # 重复输入一次密码
    password2 = serializers.CharField(min_length=6, max_length=100,
                                      error_messages={
                                          'min_length': '密码不能少于6位'
                                      })

    # 验证两次密码是否一致
    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError({'password': "两次密码不一致"})
        return attrs

    def create(self, validated_data):
        exhibitor = Exhibitors()
        exhibitor.username = validated_data.get('username')

        # 对密码加密
        password = validated_data.get('password')
        password = make_password(password)
        exhibitor.password = password

        exhibitor.company = validated_data.get('company')
        exhibitor.section = validated_data.get('section')
        exhibitor.contact = validated_data.get('contact')
        exhibitor.tel = validated_data.get('tel')
        exhibitor.position = validated_data.get('position')
        exhibitor.nation = validated_data.get('nation')
        exhibitor.email = validated_data.get('email')
        exhibitor.address = validated_data.get('address')
        exhibitor.intro = validated_data.get('intro')
        exhibitor.save()
        return exhibitor


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        exhibitor = Exhibitors.objects.filter(username=username)
        # 判断用户是否存在
        if not exhibitor.exists():
            raise serializers.ValidationError('用户不存在')
        # 用户存在
        exhibitor = exhibitor.first()
        # 检查密码
        if not check_password(password, exhibitor.password):
            raise serializers.ValidationError('用户名或密码错误')
        return attrs


class InfoSerializer(ModelSerializer):
    class Meta:
        model = Exhibitors
        exclude = ['username', 'password']

    def update(self, instance, validated_data):
        instance.company = validated_data.get('company')
        instance.section = validated_data.get('section')
        instance.contact = validated_data.get('contact')
        instance.tel = validated_data.get('tel')
        instance.position = validated_data.get('position')
        instance.nation = validated_data.get('nation')
        instance.email = validated_data.get('email')
        instance.address = validated_data.get('address')
        instance.intro = validated_data.get('intro')
        instance.save()
        return instance


class PwdSerializer(ModelSerializer):
    class Meta:
        model = Exhibitors
        fields = ['pwd', 'new_pwd', 'new_pwd2']

    pwd = serializers.CharField(min_length=6, max_length=100,
                                     error_messages={
                                         'min_length': '密码不能少于6位'
                                     })
    # 重复两次新密码
    new_pwd = serializers.CharField(min_length=6, max_length=100,
                                      error_messages={
                                          'min_length': '密码不能少于6位'
                                      })
    new_pwd2 = serializers.CharField(min_length=6, max_length=100,
                                      error_messages={
                                          'min_length': '密码不能少于6位'
                                      })

    def validate(self, attrs):
        pwd = attrs.get('pwd')
        new_pwd = attrs.get('new_pwd')
        new_pwd2 = attrs.get('new_pwd2')

        # 检查原密码
        if not check_password(pwd, self.instance.password):
            raise serializers.ValidationError('原密码错误')

        # 检查新密码两次是否一致
        if new_pwd != new_pwd2:
            raise serializers.ValidationError({'new_pwd': "两次密码不一致"})

        # 检查新密码是否和原密码相同
        if pwd == new_pwd:
            raise serializers.ValidationError('新密码和原密码相同')

        return attrs

    def update(self, instance, validated_data):
        new_pwd = validated_data.get('new_pwd')
        new_pwd = make_password(new_pwd)
        instance.password = new_pwd
        instance.save()
        return instance
