"""
URL configuration for eventApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from authApp import views as auth_views
from securityApp import views as security_views
from eventActorsApp import views as event_actors_views


urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('register/', auth_views.UserCreateView.as_view()),
    path('roles/', security_views.RoleListView.as_view()),
    path('organizators/', event_actors_views.OrganizatorCreateListView.as_view()),
    path('organizators/<str:pk>/', event_actors_views.OrganizatorDetailView.as_view()),
]
