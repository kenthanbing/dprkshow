#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@author:
@contact:
@file:ContactusSerializers.py.py
@time:2020/12/29 0029 20:04
"""
from rest_framework.serializers import ModelSerializer

from contactus.models import Contactus


class SubmitSerializer(ModelSerializer):
    class Meta:
        model = Contactus
        fields = '__all__'
