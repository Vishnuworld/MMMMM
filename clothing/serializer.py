from clothing.models import *
from rest_framework.serializers import ModelSerializer


class ProdSer(ModelSerializer):
    pass

    class Meta:
        model = Product
        fields = '__all__'


class VendSer(ModelSerializer):
    pass

    class Meta:
        model = Vendor
        fields = '__all__'



