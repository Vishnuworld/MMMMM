from django.shortcuts import render
from clothing.models import *
from clothing.serializer import *
from rest_framework import serializers, response, status, renderers, permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import list_route,action
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.authtoken.views import obtain_auth_token   #  The DRF provide an endpoint for the users to request an authentication token using their username and password

# Create your views here.
# ----------------------
# For practice, reference- https://simpleisbetterthancomplex.com/tutorial/2018/11/22/how-to-implement-token-authentication-using-django-rest-framework.html

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        content = {'message':'Hello,Vishnu!'}
        return Response(content)
#------------------------------------------------------------

class ProdVset(ModelViewSet):   # clothing

    queryset = Product.objects.all()
    serializer_class = ProdSer
    # permission_classes = (permissions.IsAuthenticated,)   # Specific for the class..In Swagger, this url can not be reflected without login.

    # def highlight(self, request, *args, **kwargs):
    #     queryset = models.objects.all()
    #
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)

    # @list_route(renderer_classes=[renderers.StaticHTMLRenderer])


    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())
    #
    #     page = self.paginate_queryset(queryset)
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         return self.get_paginated_response(serializer.data)
    #
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)

    # @action(detail=False, methods=['GET'], name='Get Highlight')
    # def highlight(self, request, *args, **kwargs):
    #     queryset = models.Highlight.objects.all()
    #
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)

#---------------------------------Final Delete
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # print(instance.__dict__)
        # instance.price=500
        # if instance.active==1:
        instance.active = 0
        instance.save()


        return Response(status=status.HTTP_204_NO_CONTENT)

#--------------------------------Final Get all

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        print(queryset)
        my_list=[]
        for item in queryset:
            if item.active==1:
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


#
# class SnippetViewSet(ModelViewSet):
#     pass
#
#     @action(detail=False, methods=['GET'], name='Get Highlight')
#     def highlight(self, request, *args, **kwargs):
#         queryset = models.Highlight.objects.all()
#
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)
#

    # --------------------------------Final Get all



class VendVset(ModelViewSet):     # vendor
    queryset = Vendor.objects.all()
    serializer_class = VendSer
    # permission_classes = (permissions.IsAuthenticated,)  # Specific for the class..This url can not be reflected without login.

    # ---------------------------------Final Delete
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        # print(instance.__dict__)
        # instance.price=500
        # if instance.active==1:
        instance.active = 0
        instance.save()

        return Response(status=status.HTTP_204_NO_CONTENT)

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

# from django.core.mail import send_mail
# from django.http import HttpResponse
# from ecommerce import settings
#
# def sendemail(request,recipient_list):
#     subject = 'Regarding Django Project'
#     message = 'How we can send the mail in Django??'
#     email_from = settings.EMAIL_HOST_USER
#     # recipient_list = ['vbhandari9561@gmail.com']
#
#     result = send_mail(subject, message, email_from, [recipient_list])
#     return HttpResponse('%s'%result)






