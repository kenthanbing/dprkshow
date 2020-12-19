#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@author:
@contact:
@file:ArticlesSerializers.py
@time:2020/12/9 0009 15:33
"""
from rest_framework import serializers

from articles.models import Articles


class ArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = "__all__"