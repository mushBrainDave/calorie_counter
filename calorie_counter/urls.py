"""efs_rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from calorie import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', obtain_jwt_token),
    path('auth/', include('djoser.urls')),
    path('', views.intake_list),
    url(r'^api/settings/$', views.getSetting),
    path('intake/', views.intake_list),
    url(r'^api/intake/$', views.intake_list),
    url(r'^api/intake/(?P<pk>[0-9]+)$', views.getIntake),
    url(r'^api/intakes/(?P<pk>[\w\-]+)$', views.intake_list_date)
]
