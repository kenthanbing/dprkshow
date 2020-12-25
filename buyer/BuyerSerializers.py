#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@author:
@contact:
@file:BuyerSerializers.py
@time:2020/12/23 0023 9:31
"""
from rest_framework.serializers import ModelSerializer

from buyer.models import Buyers


class SubmitSerializer(ModelSerializer):
    class Meta:
        model = Buyers
        fields = '__all__'

    def create(self, validated_data):
        buyer = Buyers()
        buyer.company = validated_data.get('company')
        buyer.section = validated_data.get('section')
        buyer.contact = validated_data.get('contact')
        buyer.tel = validated_data.get('tel')
        buyer.position = validated_data.get('position')
        buyer.nation = validated_data.get('nation')
        buyer.email = validated_data.get('email')
        buyer.address = validated_data.get('address')
        buyer.intro = validated_data.get('intro')
        buyer.save()
        return buyer
