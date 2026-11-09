"""
URL configuration for godCat project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from rest_framework.routers import DefaultRouter
from CATspirations.views import TheocatViewSet
# from CATspirations.views import TheocatView
from PURRmission.views import AuthUser
from django.views.generic import TemplateView

# from rest_framework.authtoken import views as auth_views

router = DefaultRouter()
router.register(r'CATspirations', TheocatViewSet, basename="theocat")
router.register(r'PURRmission', AuthUser, basename="ath_testing")

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    
    path('api/', include(router.urls)),
    
    # path("api/CATspirations/", TheocatView.as_view(), name="all-theories")
]
