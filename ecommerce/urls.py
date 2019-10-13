"""ecommerce URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view
from clothing.urls import *
from electronics.urls import *
from clothing import views

schema_view = get_swagger_view(title='Ecommerce')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('clothing', include(router.urls)),
    path('electronics', include(router1.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'', schema_view),
    path('hello/',views.HelloView.as_view(),name='hello'),
    path('api-token-auth/',obtain_auth_token,name='api_token_auth'),
    # url(r'^simpleemail/(?P<emailto>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/', 'sendSimpleEmail' , name='sendSimpleEmail')
    # path('snippets/', include(router.urls))
]
