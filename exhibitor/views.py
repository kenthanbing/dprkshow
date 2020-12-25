from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView, RetrieveUpdateAPIView, UpdateAPIView
from rest_framework.response import Response

from exhibitor.ExhibitorSerializers import RegisterSerializer, LoginSerializer, InfoSerializer, PwdSerializer
from exhibitor.models import Exhibitors
from exhibitor.util import token_confirm


class ExhibitorRegisterView(CreateAPIView):
    queryset = Exhibitors.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        # 反向序列化
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            exhibitor = serializer.save()
            return Response({
                'code': 200,
                'msg': '注册成功',
                'data': {'eid': exhibitor.eid}
            })
        return Response({
            'code': 105,
            'msg': '注册失败',
            'data': {'info': serializer.errors}
        })


class ExhibitorLoginView(GenericAPIView):
    queryset = Exhibitors.objects.all()
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # 拿到exhibitor实例
            username = serializer.data.get('username')
            exhibitor = Exhibitors.objects.filter(username=username).first()
            # 生成token
            token = token_confirm.generate_validate_token(exhibitor.eid)
            return Response({'code': status.HTTP_200_OK,
                             'msg': '登录成功',
                             'data': {
                                 'eid': exhibitor.eid,
                                 'token': token,
                                 'username': exhibitor.username
                             }})
        else:
            return Response({'code': 1004, 'msg': '校验参数错误',
                             'data': {'error': serializer.errors, 'token': None}})


class ExhibitorInfoView(RetrieveUpdateAPIView):
    queryset = Exhibitors.objects.all()
    serializer_class = InfoSerializer

    def get(self, request, *args, **kwargs):
        # 从地址栏参数获取eid
        eid = request.query_params.get('eid')
        try:
            exhibitor = Exhibitors.objects.get(pk=eid)
        except Exception as e:
            print(e)
            return Response({
                'code': 107,
                'msg': '该用户不存在',
                'data': {}
            })
        # 序列化
        serializer = InfoSerializer(instance=exhibitor)
        return Response({
            'code': status.HTTP_200_OK,
            'msg': '查询成功',
            'data': {
                'info': serializer.data
            }
        })

    def put(self, request, *args, **kwargs):
        eid = request.query_params.get('eid')
        exhibitor = Exhibitors.objects.get(pk=eid)
        serializer = self.get_serializer(instance=exhibitor, data=request.data)
        if serializer.is_valid():
            exhibitor = serializer.save()
            return Response({
                'code': 200,
                'msg': '修改信息成功',
                'data': {'eid': exhibitor.eid}
            })
        return Response({
            'code': 105,
            'msg': '修改信息失败',
            'data': {'info': serializer.errors}
        })


class ExhibitorPwdView(UpdateAPIView):
    queryset = Exhibitors.objects.all()
    serializer_class = PwdSerializer

    def put(self, request, *args, **kwargs):
        eid = request.query_params.get('eid')
        exhibitor = Exhibitors.objects.get(pk=eid)
        serializer = self.get_serializer(instance=exhibitor, data=request.data)
        if serializer.is_valid():
            exhibitor = serializer.save()
            return Response({
                'code': 200,
                'msg': '修改密码成功',
                'data': {'eid': exhibitor.eid}
            })
        return Response({
            'code': 105,
            'msg': '修改密码失败',
            'data': {'info': serializer.errors}
        })
