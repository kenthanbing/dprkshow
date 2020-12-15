from django.shortcuts import render

# Create your views here.
from rest_framework.generics import RetrieveAPIView

from articles.ArticlesSerializers import ArticlesSerializer
from articles.models import Articles


class ArticleRetrieveView(RetrieveAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
