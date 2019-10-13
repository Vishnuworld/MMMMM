from clothing.views import *
from rest_framework import routers
from django.urls import path

from rest_framework.decorators import action






router = routers.DefaultRouter()
router.register(r'products', ProdVset)
router.register(r'vendors', VendVset)
# router.register(r'snippets', SnippetViewSet)


urlpatterns = router.urls
