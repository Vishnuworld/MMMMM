from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from electronics.models import *
from electronics.serializer import *
# Create your views here.


class EvendVset(ModelViewSet):
    queryset = EVend.objects.all()
    serializer_class = EVendSer

# ---------------------------------Final Delete

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # print(instance.__dict__)
        # instance.price=500
        # if instance.active==1:
        instance.active = 0
        instance.save()

        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------Final Get all

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        print(queryset)
        my_list = []
        for item in queryset:
            if item.active == 1:
                my_list.append(item)
                item.__dict__.pop('_state')
                print(item.__dict__)
                print(item.active)

        page = self.paginate_queryset(my_list)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class EprodVset(ModelViewSet):
    queryset = EProd.objects.all()
    serializer_class = EProdSer

# ---------------------------------Final Delete
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # print(instance.__dict__)
        # instance.price=500
        # if instance.active==1:
        instance.active = 0
        instance.save()

        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------Final Get all

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        print(queryset)
        my_list = []
        for item in queryset:
            if item.active == 1:
                my_list.append(item)
                item.__dict__.pop('_state')
                print(item.__dict__)
                print(item.active)

        page = self.paginate_queryset(my_list)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
