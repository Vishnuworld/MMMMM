from electronics.models import *
from rest_framework.serializers import ModelSerializer


class EProdSer(ModelSerializer):
    pass

    class Meta:
        model = EProd
        fields = '__all__'


class EVendSer(ModelSerializer):
    pass

    class Meta:
        model = EVend
        fields = '__all__'



