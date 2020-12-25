#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: util.py
@time: 2020/3/18 11:09 上午
'''

from itsdangerous import URLSafeTimedSerializer as usts
import base64
from django.conf import settings as django_settings

from secrets import SECRET_KEY


class Token:
    def __init__(self, security_key):
        self.security_key = security_key
        self.salt = base64.encodebytes(security_key.encode('utf8'))

    # 生成token
    def generate_validate_token(self, uid):
        serializer = usts(self.security_key)
        return serializer.dumps(uid, self.salt)

    # 验证token
    def confirm_validate_token(self, token, expiration=3600):
        serializer = usts(self.security_key)
        return serializer.loads(token, salt=self.salt, max_age=expiration)


# 定义为全局变量
token_confirm = Token(SECRET_KEY)
