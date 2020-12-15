import math
from collections import OrderedDict

from django.shortcuts import render

# Create your views here.
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from articles.models import Articles
from articles.ArticlesSerializers import ArticlesSerializer


# 分页器
class ArticlesPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'size'
    page_query_param = 'page'

    def get_paginated_response(self, data):
        # 最后一页页码
        last_page = math.ceil(self.page.paginator.count / self.page_size)
        # 把所有页码放入列表中
        pages = []
        for i in range(1, last_page+1):
            pages.append(str(i))
        # 返回带有页码列表的响应
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('pages', pages),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
        ]))


class ArticlesListView(ListAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
    pagination_class = ArticlesPagination
    # backend 中加入OrderingFilter 激活ordering filter，字段为ordering

    filter_backends = (OrderingFilter,)
    ordering_fields = ('aid',)
    # 指定默认的排序字段
    ordering = ('aid',)

    # authentication_classes = 未鉴权
    # permission_classes = 未鉴权
    #
    # def list(self, request, *args, **kwargs):
    #     queryset = self.get_queryset()
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response({
    #         'code': '200',
    #         'msg': '查询成功',
    #         'data': serializer.data
    #     })
