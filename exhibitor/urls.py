"""dprkshow URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include

from exhibitor import views

app_name = 'exhibitor'

urlpatterns = [
    path('info/', views.ExhibitorInfoView.as_view(), name='info'),
    path('register/', views.ExhibitorRegisterView.as_view(), name='register'),
    path('login/', views.ExhibitorLoginView.as_view(), name='loglin'),
    path('pwd/', views.ExhibitorPwdView.as_view(), name='pwd')

]
