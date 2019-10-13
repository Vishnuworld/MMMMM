from clothing.views import *
from rest_framework import routers
from electronics.views import *


router1 = routers.DefaultRouter()
router1.register(r'eproducts', EprodVset)
router1.register(r'evendors', EvendVset)


urlpatterns = router1.urls
