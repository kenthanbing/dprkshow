from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from buyer.BuyerSerializers import SubmitSerializer
from buyer.models import Buyers


class BuyerSubmitView(CreateAPIView):
    queryset = Buyers.objects.all()
    serializer_class = SubmitSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            buyer = serializer.save()
            return Response({
                'code': 200,
                'msg': '注册成功',
                'data': {'bid': buyer.bid}
            })
        return Response({
            'code': 105,
            'msg': '注册失败',
            'data': {'info': serializer.errors}
        })
