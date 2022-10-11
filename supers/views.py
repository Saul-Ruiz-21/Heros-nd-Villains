from django.shortcuts import get_object_or_404
from urllib import response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import supers
from .models import Super
from .serializers import SuperSerializer
from supers import serializers

@api_view(['GET', 'POST'])
def supers_list(request):

    if request.method == 'GET':
        super = Super.objects.all()
        serializer = SuperSerializer(super, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SuperSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)

