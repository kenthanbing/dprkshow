from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView

from contactus.ContactusSerializers import SubmitSerializer
from contactus.models import Contactus


class ContactusSubmitView(CreateAPIView):
    queryset = Contactus.objects.all()
    serializer_class = SubmitSerializer
